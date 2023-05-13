use fixedbitset::FixedBitSet;
use itertools::Itertools;
use lazy_static::lazy_static;
use regex::Regex;
use std::{fmt, str::FromStr};

use num_traits::{FromPrimitive, ToPrimitive};

// Control signals defenitions
#[derive(Primitive, Debug, Clone, Copy)]
pub enum BaseCs {
    /// Read Data Register
    RDDR = 0,
    /// Read Command Register
    RDCR = 1,
    /// Read Instruction Pointer
    RDIP = 2,
    /// Read Stack Pointer
    RDSP = 3,
    /// Read Accumulator
    RDAC = 4,
    /// Read Buffer Register
    RDBR = 5,
    /// Read Program State register
    RDPS = 6,
    /// Read Input Register
    RDIR = 7,
    /// Complement Right input
    COMR = 8,
    /// Complement Left input
    COML = 9,
    /// Plus one
    PLS1 = 10,
    /// Summary OR And
    SORA = 11,
    /// Lower byte to lower
    LTOL = 12,
    /// Lower byte to high
    LTOH = 13,
    /// High byte to lower
    HTOL = 14,
    /// High byte to high
    HTOH = 15,
    /// Sign Extend from lower byte to high
    SEXT = 16,
    /// SHift Left
    SHLT = 17,
    /// Use old C as value for 0th bit (SH_L + SHL0 == ROL)
    SHL0 = 18,
    /// SHift RighT
    SHRT = 19,
    /// ???
    SHRF = 20,
    /// Set flag C
    SETC = 21,
    /// Set flag oVerflow
    SETV = 22,
    /// Set flags N and Z
    STNZ = 23,
    /// Write to Data Register
    WRDR = 24,
    /// Write to Command Register
    WRCR = 25,
    /// Write to Instruction Pointer
    WRIP = 26,
    /// Write to Stack Pointer
    WRSP = 27,
    /// Write to Accumulator
    WRAC = 28,
    /// Write to Buffer Register
    WRBR = 29,
    /// Write to Program State register
    WRPS = 30,
    /// Write to Address Register
    WRAR = 31,
    /// Load value from Memory to Data Register
    LOAD = 32,
    /// Store value from Data Register to Memory
    STOR = 33,
    /// Input output
    IO = 34,
    ///
    INTS = 35,
    /// Reserved
    RESERVED36 = 36,
    /// Reserved
    RESERVED37 = 37,
    /// HALT
    HALT = 38,
}

#[derive(Clone, Copy)]
pub enum Cs {
    Base(BaseCs),
    Bit(u8),
    Addr(u8),
    Comp(bool),
    Type(bool),
}

impl fmt::Debug for Cs {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            Cs::Base(base) => write!(f, "{base:?}"),
            Cs::Bit(bit) => write!(f, "bit {bit:08b}"),
            Cs::Addr(addr) => write!(f, "addr {addr:02x}"),
            Cs::Comp(comp) => write!(f, "comp {}", comp as u8),
            Cs::Type(mc_type) => write!(f, "TYPE {}", mc_type as u8),
        }
    }
}
impl BaseCs {
    pub fn update_state(&self, state: &mut u64) {
        *state |= 1 << self.to_u64().unwrap();
    }
}
