use enum_iterator::IntoEnumIterator;
use int_enum::IntEnum;

#[repr(usize)]
#[derive(Clone, Copy, Debug, PartialEq, IntEnum, IntoEnumIterator)]
pub enum ResistorColor {
    Black = 0,
    Brown = 1,
    Red = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Blue = 6,
    Violet = 7,
    Grey = 8,
    White = 9,
}

pub fn color_to_value(_color: ResistorColor) -> usize {
    _color.int_value()
}

pub fn value_to_color_string(value: usize) -> String {
    match ResistorColor::from_int(value) {
        Ok(ResistorColor::Black) => String::from("Black"),
        Ok(ResistorColor::Blue) => String::from("Blue"),
        Ok(ResistorColor::Brown) => String::from("Brown"),
        Ok(ResistorColor::Green) => String::from("Green"),
        Ok(ResistorColor::Grey) => String::from("Grey"),
        Ok(ResistorColor::Orange) => String::from("Orange"),
        Ok(ResistorColor::Red) => String::from("Red"),
        Ok(ResistorColor::Violet) => String::from("Violet"),
        Ok(ResistorColor::White) => String::from("White"),
        Ok(ResistorColor::Yellow) => String::from("Yellow"),
        Err(_) => String::from("value out of range"),
    }
}

pub fn colors() -> Vec<ResistorColor> {
    ResistorColor::into_enum_iter().collect::<Vec<ResistorColor>>()
}
