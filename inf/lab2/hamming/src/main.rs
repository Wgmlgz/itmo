use regex::Regex;
use std::io::stdin;

fn main() {
    let size = 8;

    loop {
        println!("Enter binary string of length {}:", size - 1);
        let mut s = String::new();
        stdin().read_line(&mut s).unwrap();
        s = s.trim().to_string();

        if !Regex::new(format!("^[01]{{{}}}$", size - 1).as_str())
            .unwrap()
            .is_match(&s)
        {
            println!("Invalid string (\n");
            continue;
        }

        let mut v = s
            .chars()
            .map(|ch| ch.to_digit(2).unwrap() == 1)
            .collect::<Vec<_>>();
        v.insert(0, false);

        let err = v
            .iter()
            .cloned()
            .enumerate()
            .filter_map(|(idx, bit)| bit.then(|| idx))
            .reduce(|a, b| a ^ b)
            .unwrap_or_else(|| 0);

        if err == 0 {
            print!("No error detected! Message: ");
        } else {
            v[err] ^= true;
            print!(
                "Error at position {} found and corrected: ",
                match err.count_ones() {
                    0 => format!("_"),
                    1 => format!("r{}", err.trailing_zeros() + 1),
                    _ => format!("i{}", err - (err as f64).log2().ceil() as usize),
                }
            );
        }

        println!(
            "{}\n",
            v.iter()
                .enumerate()
                .filter_map(|(idx, x)| (idx.count_ones() > 1).then(|| (*x as i32).to_string()))
                .collect::<String>()
        );
    }
}
