use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");

    let mut iter = input.split_whitespace();
    let a:i32 = iter.next().unwrap().parse().expect("");
    let b:i32 = iter.next().unwrap().parse().expect("");
    let result = a + b;
    println!("{}",result)
}