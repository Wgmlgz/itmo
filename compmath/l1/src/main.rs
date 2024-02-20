use anyhow::{anyhow, Result};
use clap::Parser;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};

fn read_matrix_from_file(path: &str) -> Result<(Vec<Vec<f64>>, Vec<f64>, f64)> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let mut lines = reader.lines();

    let n: usize = lines
        .next()
        .ok_or(anyhow!("expected matrix size"))??
        .parse()?; // Считываем размерность матрицы
    let mut a = vec![vec![0.0; n]; n];
    let mut b = vec![0.0; n];

    for (i, line) in lines.by_ref().take(n).enumerate() {
        let row: Result<Vec<f64>> = line?
            .split_whitespace()
            .map(|x| x.parse().map_err(|_| anyhow!("Неверный формат числа")))
            .collect();
        let row = row?;
        for (j, &val) in row.iter().enumerate().take(n) {
            a[i][j] = val;
        }
    }

    for (i, line) in lines.by_ref().take(n).enumerate() {
        b[i] = line?.parse()?;
    }

    let tolerance: f64 = lines
        .next()
        .ok_or(anyhow!("expected tolerance"))??
        .parse()?; // Считываем заданную точность

    Ok((a, b, tolerance))
}

fn read_matrix_from_input() -> Result<(Vec<Vec<f64>>, Vec<f64>, f64)> {
    let mut input = String::new();
    println!("Введите размерность матрицы n (<=20):");
    io::stdin().read_line(&mut input)?;
    let n: usize = input.trim().parse()?;

    let mut a = vec![vec![0.0; n]; n];
    let mut b = vec![0.0; n];

    for i in 0..n {
        println!(
            "Введите {} коэффициенты {}-й строки матрицы A, разделенные пробелом:",
            n,
            i + 1
        );
        input.clear();
        io::stdin().read_line(&mut input)?;
        let row: Result<Vec<f64>> = input
            .split_whitespace()
            .map(|x| x.parse().map_err(|_| anyhow!("Неверный формат числа")))
            .collect();
        let row = row?;

        a[i] = row;
    }

    for i in 0..n {
        println!("Введите значение {}-го элемента вектора B:", i + 1);
        input.clear();
        io::stdin().read_line(&mut input)?;
        b[i] = input.trim().parse()?;
    }

    println!("Введите заданную точность:");
    input.clear();
    io::stdin().read_line(&mut input)?;
    let tolerance: f64 = input.trim().parse()?;

    Ok((a, b, tolerance))
}

fn check_and_swap_for_diagonal_dominance(a: &mut Vec<Vec<f64>>, b: &mut Vec<f64>) -> bool {
    let is_diagonally_dominant = |row: &Vec<f64>, index: usize| -> bool {
        row[index].abs()
            > row
                .iter()
                .enumerate()
                .map(|(j, val)| if j != index { val.abs() } else { 0.0 })
                .sum::<f64>()
    };

    let n = a.len();
    let mut swapped;
    for i in 0..n {
        swapped = false;
        if !is_diagonally_dominant(&a[i], i) {
            for j in i + 1..n {
                if is_diagonally_dominant(&a[j], i) {
                    a.swap(i, j);
                    b.swap(i, j);
                    swapped = true;
                    break;
                }
            }
            if !swapped {
                return false;
            }
        }
    }
    true
}

fn gauss_seidel(
    a: Vec<Vec<f64>>,
    b: Vec<f64>,
    tolerance: f64,
    m: usize,
) -> (Vec<f64>, usize, Vec<Vec<f64>>) {
    let n = a.len();
    let mut x = vec![0.0; n];
    let mut x_prev = x.clone();
    let mut num_iterations = 0;
    let mut errors = vec![vec![0.0; n]];

    for _ in 0..m {
        let mut max_error: f64 = 0.0;
        errors.push(vec![0.0; n]);
        for i in 0..n {
            let sum: f64 = (0..n).filter(|&j| j != i).map(|j| a[i][j] * x[j]).sum();
            x_prev[i] = x[i];
            x[i] = (b[i] - sum) / a[i][i];
            let err = (x[i] - x_prev[i]).abs();
            errors[num_iterations][i] = err; // Вычисляем абсолютную погрешность для каждой переменной
            max_error = max_error.max(err);
        }
        num_iterations += 1;

        if max_error < tolerance {
            errors.pop();
            break;
        }
    }

    (x, num_iterations, errors)
}

// fn matrix_norm(
//     a: Vec<Vec<f64>>,
//     b: Vec<f64>,
// ) -> (Vec<f64>, usize, Vec<Vec<f64>>) {
//     let n = a.len();
//     let c = a.clone();
//     for i in 0..n {
//     }
// }

fn print_errors(errors: Vec<Vec<f64>>) {
    println!("История погрешностей по итерациям:");
    for (iteration, errs) in errors.iter().enumerate() {
        print!("Итерация {}: ", iteration + 1);
        print_v(errs);
    }
}

fn print_v(a: &Vec<f64>) {
    for item in a {
        print!("{:5.2} ", item);
    }
    println!();
}

fn print_matrix(a: &Vec<Vec<f64>>) {
    for row in a {
        print_v(row);
    }
}

#[derive(Parser)]
#[clap(author = "Wgmlgz", version = "1.0", about = "Gauss-Seidel Solver")]
struct Args {
    /// Sets a custom input file
    #[clap(short, long, value_parser)]
    input: Option<String>,
}

fn solve() -> Result<()> {
    let args = Args::parse();

    let (mut a, mut b, tolerance) = if let Some(file) = args.input {
        let res =
            read_matrix_from_file(file.as_str()).map_err(|_| anyhow!("Неверный формат ввода"))?;
        println!("Read data from file: {}", file);
        res
    } else {
        let res = read_matrix_from_input()?;
        println!("Read data from standard input");
        res
    };

    if !check_and_swap_for_diagonal_dominance(&mut a, &mut b) {
        println!("Диагональное преобладание не достигнуто.");
        // return Ok(());
    }

    println!("Решение на матрице:");
    print_matrix(&a);

    let m = 100;
    let (x, num_iterations, errors) = gauss_seidel(a, b, tolerance, m);

    print!("Решение: ");
    print_v(&x);
    println!("Количество итераций: {}", num_iterations);
    print_errors(errors);

    Ok(())
}
fn main() {
    // env::set_var("RUST_BACKTRACE", "1");
    if let Err(e) = solve() {
        println!("{}", e.to_string());
    }
}
