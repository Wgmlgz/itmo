use std::rc::{Rc, Weak};

type Args<const N: usize> = [bool; N];
struct BoolFn {
    n: usize,
    name: String,
    print: fn(args: &[bool]) -> String,
    eval: fn(args: &[bool]) -> bool,
}

#[derive(Clone)]
enum BoolExp {
    Val(Rc<bool>),
    Exp(Rc<BoolFn>, Vec<Box<BoolExp>>),
}

trait IntoBoolExp {
    fn into(self) -> Box<BoolExp>;
}

impl BoolExp {
    fn eval_args(&self) -> Vec<bool> {
        match self {
            Self::Val(x) => panic!("sussy baka"),
            Self::Exp(f, args) => (*args).iter().map(|x| x.eval()).collect::<Vec<_>>(),
        }
    }
    fn eval(&self) -> bool {
        match self {
            Self::Val(x) => **x,
            Self::Exp(f, args) => (f.eval)(self.eval_args().as_slice()),
        }
    }
    fn to_string(&self) -> String {
        match self {
            Self::Val(x) => format!("{}", **x as i32),
            Self::Exp(f, args) => (f.print)(self.eval_args().as_slice()),
        }
    }
    fn test(&self) {
        println!("sus")
    }
    fn new_from_tuple<T>(t: T) -> Vec<Self> {
        todo!()
    }
    fn new<T>(args: T) -> Box<Self>
    where
        T: IntoBoolExp,
    {
        args.into()
        // let v = child.iter().map(|&x| Box::new(x)).collect::<Vec<_>>();
        // BoolExp::Exp(f, v)
    }
}

impl IntoBoolExp for (Rc<BoolFn>, &[Box<BoolExp>]) {
    fn into(self) -> Box<BoolExp> {
        Box::new(BoolExp::Exp(self.0, self.1.to_vec()))
    }
}

impl IntoBoolExp for Rc<BoolFn> {
    fn into(self) -> Box<BoolExp> {
        Box::new(BoolExp::Val(Rcself))
    }
}
impl IntoBoolExp for bool {
    
}

fn print_table(f: &BoolFn) {
    println!("{}", f.name);
    for line in 0usize..(1 << f.n) {
        let mut args = vec![false; f.n];
        for i in 0..f.n {
            let bit = (line & (1 << i)) != 0;
            args[i] = bit;
        }
        println!("{} = {}", (f.print)(&args), (f.eval)(&args) as i32);
    }
}

macro_rules! sus {
    ($args:tt, $e:expr) => {
        |arr| match arr {
            $args => $e,
            _ => panic!(),
        }
    };
}

macro_rules! sus {
    ($args:tt, $e:expr) => {
        |arr| match arr {
            $args => $e,
            _ => panic!(),
        }
    };
}

fn main() {
    let or = Rc::new(BoolFn {
        n: 2,
        name: "or".into(),
        print: sus!([a, b], format!("{} | {}", *a as i32, *b as i32)),
        eval: sus!([a, b], a | b),
    });
    let and = Rc::new(BoolFn {
        n: 2,
        name: "and".into(),
        print: sus!([a, b], format!("{} & {}", *a as i32, *b as i32)),
        eval: sus!([a, b], a & b),
    });
    let not = BoolFn {
        n: 2,
        name: "and".into(),
        print: sus!([a], format!("!{}", *a as i32)),
        eval: sus!([a], !a),
    };

    let v = vec![or.clone(), and.clone()];

    use BoolExp::{Exp, Val};

    let e = BoolExp::new(true);
    let e = BoolExp::new((
        or.clone(),
        &[and.clone(), or.clone()] as &[Rc<BoolFn>],
    ));
    println!("{}", e.to_string());
    for f in v {
        print_table(&f);
    }
}
