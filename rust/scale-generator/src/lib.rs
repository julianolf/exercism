const SHARPS: &[&str] = &["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"];
const FLATS: &[&str] = &["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"];

#[derive(Debug)]
pub enum Error {
    InvalidTonic,
    InvalidInterval,
}

#[derive(Debug)]
pub struct Scale {
    notes: Vec<String>,
}

impl Scale {
    pub fn new(tonic: &str, intervals: &str) -> Result<Scale, Error> {
        let scale = match tonic {
            "C" | "a" | "G" | "D" | "A" | "E" | "B" | "F#" | "e" | "b" | "f#" | "c#" | "g#" | "d#" => SHARPS,
            "F" | "Bb" | "Eb" | "Ab" | "Db" | "Gb" | "d" | "g" | "c" | "f" | "bb" | "eb" => FLATS,
            _ => return Err(Error::InvalidTonic),
        };

        let mut idx = scale
            .iter()
            .position(|&n| n.to_uppercase() == tonic.to_uppercase())
            .unwrap();

        let mut notes = Vec::with_capacity(intervals.len());

        notes.push(scale[idx].to_string());

        for chr in intervals.chars() {
            idx += match chr {
                'm' => 1,
                'M' => 2,
                'A' => 3,
                _ => return Err(Error::InvalidInterval),
            };

            notes.push(scale[idx % scale.len()].to_string());
        }

        Ok(Scale { notes })
    }

    pub fn chromatic(tonic: &str) -> Result<Scale, Error> {
        Scale::new(tonic, "mmmmmmmmmmmm")
    }

    pub fn enumerate(&self) -> Vec<String> {
        self.notes.clone()
    }
}
