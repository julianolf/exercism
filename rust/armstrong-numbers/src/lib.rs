pub fn is_armstrong_number(num: u32) -> bool {
    let digits = num.to_string();
    let length = digits.len() as u32;

    digits
        .chars()
        .map(|d| d.to_digit(10).unwrap().saturating_pow(length))
        .fold(0, |acc: u32, e: u32| acc.saturating_add(e))
        .eq(&num)
}
