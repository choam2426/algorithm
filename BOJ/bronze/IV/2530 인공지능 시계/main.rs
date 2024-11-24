use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("");
    let mut iter = input.split_whitespace();
    let h: i32 = iter.next().unwrap().parse().expect("");
    let m: i32 = iter.next().unwrap().parse().expect("");
    let s: i32 = iter.next().unwrap().parse().expect("");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("");
    let input = input.trim();
    let cooking_time: i32 = input.parse::<i32>().expect("");
    let total_second:i32 = h * 3600 + m * 60 + s + cooking_time;
    println!("{} {} {}", total_second / 3600 % 24, total_second % 3600 / 60, total_second % 60);
}
