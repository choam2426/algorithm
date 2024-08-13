use std::io;

fn main() {
    let mut input = String.new();
    io::stdin().read_line(&mut input).expect("");
    let mut iter = input.split_whitespace();
    let r1:i32 = iter.next().unwrap().parse().expect("");
    let s:i32 = iter.next().unwrap().parse().expect("");
    let result = s * 2 - r1;
    println!("{}",result)
}