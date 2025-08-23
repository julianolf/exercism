#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    match (_first_list, _second_list) {
        (a, b) if a == b => Comparison::Equal,
        (a, _) if a.is_empty() => Comparison::Sublist,
        (_, b) if b.is_empty() => Comparison::Superlist,
        (a, b) if b.windows(a.len()).any(|x| x == a) => Comparison::Sublist,
        (a, b) if a.windows(b.len()).any(|x| x == b) => Comparison::Superlist,
        _ => Comparison::Unequal,
    }
}
