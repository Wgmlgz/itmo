mod control_signals;
mod regexes;
mod table;
mod tests;

use control_signals::{
    BaseCs::{self, *},
    Cs::{self, *},
};
use fancy_regex::{Match, Regex};
use fixedbitset::FixedBitSet;
use itertools::Itertools;
use lazy_static::lazy_static;
use regexes::*;
use std::{collections::HashMap, error::Error, ops::Range, str::FromStr};
type ParseErr = Box<dyn Error>;
type ParseRes = Result<Command, ParseErr>;

#[macro_use]
extern crate enum_primitive_derive;
extern crate num_traits;

use num_traits::{FromPrimitive, ToPrimitive, Zero};

#[derive(Default)]
pub struct Command {
    pub cmd: u64,
}

impl Command {
    fn new(cmd: u64) -> Self {
        Self { cmd }
    }
    fn cs(&self) -> Vec<Cs> {
        let mc_type = !(self.cmd & (1 << 39)).is_zero();
        let mut v = (if mc_type { 0..16 } else { 0..39 })
            .filter_map(|bit| {
                (!(self.cmd & (1 << bit)).is_zero()).then(|| Base(BaseCs::from_usize(bit).unwrap()))
            })
            .collect_vec();
        if mc_type {
            v.push(Bit(((self.cmd >> 16) & 0xff) as u8));
            v.push(Addr(((self.cmd >> 24) & 0x7f) as u8));
            v.push(Comp(((self.cmd >> 33) & 0x1) != 0));
        }
        v.push(Type(mc_type));

        v
    }
}

#[derive(Default)]
pub struct ParseState {
    pub cmd: u64,
    pub range: Range<usize>,
}

impl ParseState {
    fn add_state(&mut self, cs: Cs) {
        match cs {
            Cs::Base(base) => base.update_state(&mut self.cmd),
            Cs::Bit(bit) => self.cmd |= (bit as u64) << 16,
            Cs::Addr(addr) => self.cmd |= (addr as u64) << 24,
            Cs::Comp(comp) => self.cmd |= (comp as u64) << 33,
            Cs::Type(mc_type) => self.cmd |= (mc_type as u64) << 39,
        }
    }

    fn parse_general(&mut self, s: &str) -> ParseRes {
        dbg!("enter general");
        // just hint's for better ux
        if let Some(cap) = IF_TYPE_RE.captures(s)? {
            self.add_state(Type(true));

            let cap = IF_STRUCTURE_RE
                .captures(cap.get(2).unwrap().as_str())
                .unwrap()
                .ok_or("seems like if command, but unable to parce it")?;

            return self.parse_if(cap.get(2).unwrap(), cap.get(3).unwrap());
        } else if let Some(cap) = GOTO_TYPE_RE.captures(s)? {
            // that's how unconditional jums works lol
            self.add_state(Type(true));
            self.add_state(Base(BaseCs::RDPS));
            self.add_state(Base(BaseCs::LTOL));
            self.add_state(Bit(0b0010000));
            return self.parse_goto(cap.get(1).unwrap());
        } else {
            return self.parse_omc(s);
        }
    }

    fn parse_if(&mut self, condition: Match, goto: Match) -> ParseRes {
        dbg!("enter if");
        dbg!(condition.as_str());
        dbg!(goto.as_str());
        dbg!(IF_COND_RE.as_str());

        self.range = condition.range();

        let cap = IF_COND_RE
            .captures(condition.as_str().trim())
            .unwrap()
            .ok_or("unable to parse if condition")?;

        let huh = HashMap::from([
            // input reg
            ("RDDR", Base(BaseCs::RDDR)),
            ("RDCR", Base(BaseCs::RDCR)),
            ("RDIP", Base(BaseCs::RDIP)),
            ("RDSP", Base(BaseCs::RDSP)),
            ("RDAC", Base(BaseCs::RDAC)),
            ("RDBR", Base(BaseCs::RDBR)),
            ("RDPS", Base(BaseCs::RDPS)),
            ("RDIR", Base(BaseCs::RDIR)),
            // comp
            ("ZERO", Comp(false)),
            ("ONE", Comp(true)),
            // ("COMR", CS::COMR),
            // ("COML", CS::COML),
            // ("PLS1", CS::PLS1),
            // ("SORA", CS::SORA),

            // ("LTOL", CS::LTOL),
            // ("HTOL", CS::HTOL),

            // ("LTOL", CS::LTOL),
            // ("HTOL", CS::HTOL),

            //
            // ("SWAB", CS::TYPE),
            // ("SWAB", CS::TYPE),
        ]);
        for (name, cs) in huh {
            if let Some(mtch) = cap.name(name) {
                self.add_state(cs);
            }
        }
        self.parse_goto(goto)
    }

    fn parse_goto(&mut self, goto: Match) -> ParseRes {
        dbg!("enter goto");

        self.range = goto.range();
        let t = GOTO_RE
            .captures(goto.as_str().trim())
            .unwrap()
            .ok_or("invalid goto body")?;

        let addr = t.get(2).unwrap().as_str();
        self.add_state(Addr(u8::from_str_radix(addr, 16).map_err(|e| {
            format!("unable to parse address, must be in [00, FF], but got {addr}")
        })?));

        Ok(Command::new(self.cmd))
    }

    fn parse_omc(&mut self, s: &str) -> ParseRes {
        // self.range = omc.range();

        todo!()
    }

    //     let cap = Regex::new(format!("^{}$", MC).as_str())?
    //         .captures(s)?
    //         .ok_or("unable to parse command")?;

    //     let mut state: u64 = 0;

    //     let huh = HashMap::from([
    //         ("RDDR", CS::RDDR),
    //         ("RDCR", CS::RDCR),
    //         ("RDIP", CS::RDIP),
    //         ("RDSP", CS::RDSP),
    //         ("RDAC", CS::RDAC),
    //         ("RDBR", CS::RDBR),
    //         ("RDPS", CS::RDPS),
    //         ("RDIR", CS::RDIR),
    //         ("COMR", CS::COMR),
    //         ("COML", CS::COML),
    //         ("PLS1", CS::PLS1),
    //         ("SORA", CS::SORA),
    //         ("LTOL", CS::LTOL),
    //         ("LTOH", CS::LTOH),
    //         ("HTOL", CS::HTOL),
    //         ("HTOH", CS::HTOH),
    //         ("SEXT", CS::SEXT),
    //         ("SHLT", CS::SHLT),
    //         ("SHL0", CS::SHL0),
    //         ("SHRT", CS::SHRT),
    //         ("SHRF", CS::SHRF),
    //         ("SETC", CS::SETC),
    //         ("SETV", CS::SETV),
    //         ("STNZ", CS::STNZ),
    //         ("WRDR", CS::WRDR),
    //         ("WRCR", CS::WRCR),
    //         ("WRIP", CS::WRIP),
    //         ("WRSP", CS::WRSP),
    //         ("WRAC", CS::WRAC),
    //         ("WRBR", CS::WRBR),
    //         ("WRPS", CS::WRPS),
    //         ("WRAR", CS::WRAR),
    //         ("LOAD", CS::LOAD),
    //         ("STOR", CS::STOR),
    //         ("IO", CS::IO),
    //         ("INTS", CS::INTS),
    //         ("RESERVED36", CS::RESERVED36),
    //         ("RESERVED37", CS::RESERVED37),
    //         ("HALT", CS::HALT),
    //         ("TYPE", CS::TYPE),

    //         //
    //         // ("SWAB", CS::TYPE),
    //         // ("SWAB", CS::TYPE),

    //     ]);
    //     for (name, cs) in huh {
    //         if let Some(mtch) = cap.name(name) {
    //             cs.update_state(&mut state);
    //         }
    //     }

    //     CS::LTOL.update_state(&mut state);
    //     CS::HTOH.update_state(&mut state);

    //     let res = Command { cmd: state };

    //     Ok(res)
    //     // Err("Unknown type of command".into())
    // }

    // /// Parses Control micro code
    // fn parse_cmc(s: &str) -> ParseRes {
    //     todo!()
    // }
    // /// Parses Operational micro code
    // fn parse_omc(s: &str) -> ParseRes {
    //     let subcommands = s.split(';').map(|s| s.trim()).collect_vec();

    //     // if RE.captures("")
    //     todo!()
}
impl FromStr for Command {
    type Err = ParseErr;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        ParseState::default()
            .parse_general(s.to_uppercase().as_str())
            .into()
    }
}
// impl Command {
//     fn (s: Into<String>) {

//     }
// }

fn main() {
    dbg!(Command::new(0x81bb024002).cs());
    // let t =
    // dbg!(OMC);
    // dbg!(MC_RE.as_str());

    // dbg!(OMC);
    // let cap = ALU_RES_RE.captures("DR -> IP").unwrap();
    // let n = ALU_R_FULL_RE.capture_names();
    // dbg!(n);

    // let v = cap.iter().collect_vec();
    // dbg!(v);
    // println!("Hello, world!");
}
