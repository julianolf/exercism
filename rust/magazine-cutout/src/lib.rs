use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut source: HashMap<&str, u32> = HashMap::new();

    for word in magazine.iter() {
        source.entry(word).and_modify(|v| *v += 1).or_insert(1);
    }

    for word in note.iter() {
        match source.get_mut(word) {
            Some(v) if *v > 0 => *v -= 1,
            _ => return false,
        }
    }

    true
}
