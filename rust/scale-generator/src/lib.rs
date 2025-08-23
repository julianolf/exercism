const SHARPS: [&str; 12] = [
    "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",
];
const FLATS: [&str; 12] = [
    "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab",
];
const TONICS_NO_SHARPS_OR_FLATS: [&str; 2] = ["C", "a"];
const TONICS_FOR_SHARPS: [&str; 12] = [
    "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", "g#", "d#",
];
const TONICS_FOR_FLATS: [&str; 12] = [
    "F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb",
];
const INTERVALS: [char; 3] = ['m', 'M', 'A'];

#[derive(Debug)]
pub enum Error {
    InvalidTonic,
    InvalidInterval,
}

#[derive(Debug)]
pub struct Scale {
    tonic: String,
    intervals: String,
}

impl Scale {
    pub fn new(tonic: &str, intervals: &str) -> Result<Scale, Error> {
        if !TONICS_NO_SHARPS_OR_FLATS.contains(&tonic)
            && !TONICS_FOR_SHARPS.contains(&tonic)
            && !TONICS_FOR_FLATS.contains(&tonic)
        {
            return Err(Error::InvalidTonic);
        }

        if !intervals.chars().all(|chr| INTERVALS.contains(&chr)) {
            return Err(Error::InvalidInterval);
        }

        Ok(Scale {
            tonic: String::from(tonic),
            intervals: String::from(intervals),
        })
    }

    pub fn chromatic(tonic: &str) -> Result<Scale, Error> {
        Scale::new(tonic, "mmmmmmmmmmmm")
    }

    pub fn enumerate(&self) -> Vec<String> {
        let notes = if TONICS_FOR_FLATS.contains(&self.tonic.as_str()) {
            &FLATS
        } else {
            &SHARPS
        };

        let mut tonic_chars = self.tonic.chars();
        let first_note = match tonic_chars.next() {
            Some(chr) => chr.to_uppercase().collect::<String>() + tonic_chars.as_str(),
            None => String::new(),
        };
        let mut idx = notes
            .iter()
            .position(|&n| n == first_note.as_str())
            .unwrap();
        let mut scale = vec![first_note];

        for chr in self.intervals.chars() {
            let inc = match chr {
                'm' => 1,
                'M' => 2,
                'A' => 3,
                _ => 1,
            };

            idx = (idx + inc) % notes.len();
            scale.push(String::from(notes[idx]));
        }

        scale
    }
}
