use std::io;

fn main() {
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("");
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("");

    let num1:i32 = input1.trim().parse().expect("");
    let num2:i32 = input2.trim().parse().expect("");
    let result:i32 = num1 + num2;
    println!("{}", result);
}