use std::panic;

pub fn is_armstrong_number(num: u32) -> bool {
    let digits: Vec<u32> = num
        .to_string()
        .chars()
        .map(|d| d.to_digit(10).unwrap())
        .collect();

    let length = digits.len() as u32;

    let result = panic::catch_unwind(|| digits.iter().fold(0, |acc, d| acc + d.pow(length)));

    num == result.unwrap_or(0)
}
