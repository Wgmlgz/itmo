use regex::Regex;
use std::io::stdin;

fn main() {
    let size = 8;

    loop {
        println!("Enter binary string of length {}:", size - 1);
        let mut s = String::new();
        stdin().read_line(&mut s).unwrap();
        s = s.trim().to_string();

        if !Regex::new(format!("[01]{{{}}}", size - 1).as_str())
            .unwrap()
            .is_match(&s)
        {
            println!("Invalid string (\n");
            continue;
        }

        let mut v = s
            .chars()
            .map(|ch| ch.to_digit(2).unwrap() as usize)
            .collect::<Vec<_>>();
        v.insert(0, 0);

        let err = v
            .iter()
            .cloned()
            .enumerate()
            .filter_map(|(idx, bit)| match bit {
                1 => Some(idx),
                _ => None,
            })
            .reduce(|a, b| a ^ b)
            .unwrap();

        if err == 0 {
            println!("No error detected!");
        } else {
            v[err] ^= 1;
            v.remove(0);
            println!(
                "Error at position {err} found and corrected: {}\n",
                v.into_iter()
                    .map(|x| x.to_string())
                    .collect::<Vec<_>>()
                    .join("")
            );
        }
    }
}
