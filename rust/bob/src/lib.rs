pub fn reply(message: &str) -> &str {
    let message = message.trim();

    match (
        message.is_empty(),
        message.chars().any(char::is_alphabetic),
        message.ends_with('?'),
        message == message.to_uppercase(),
    ) {
        (true, _, _, _) => "Fine. Be that way!",
        (false, true, false, true) => "Whoa, chill out!",
        (false, true, true, true) => "Calm down, I know what I'm doing!",
        (false, _, true, _) => "Sure.",
        _ => "Whatever.",
    }
}
