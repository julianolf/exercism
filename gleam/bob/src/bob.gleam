import gleam/string
import gleam/regex

pub fn hey(remark: String) -> String {
  let assert Ok(re) = regex.from_string(".*[a-zA-Z]+.*")

  let str = string.trim(remark)
  let has_letter = regex.check(re, str)
  let asking = string.ends_with(str, "?")
  let yelling = string.uppercase(str) == str
  let nothing = string.is_empty(str)


  case has_letter, asking, yelling, nothing {
    True, False, True, False -> "Whoa, chill out!"
    True, True, True, False -> "Calm down, I know what I'm doing!"
    _, True, _, False -> "Sure."
    _, _, _, True-> "Fine. Be that way!"
    _, _, _, _ -> "Whatever."
  }
}
