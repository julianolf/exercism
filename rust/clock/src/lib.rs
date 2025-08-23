use std::fmt;

#[derive(Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:0>2}:{:0>2}", self.hours, self.minutes)
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            ..Default::default()
        }
        .add_minutes(hours * 60 + minutes)
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        let mut clock = Clock {
            hours: self.hours,
            minutes: self.minutes,
        };

        if minutes > 0 {
            let time = clock.hours * 60 + clock.minutes + minutes;

            clock.hours = time / 60 % 24;
            clock.minutes = time % 60;
        } else if minutes < 0 {
            let mut count = minutes;

            while count < 0 {
                clock.minutes -= 1;

                if clock.minutes < 0 {
                    clock.minutes = 59;
                    clock.hours -= 1;

                    if clock.hours < 0 {
                        clock.hours = 23;
                    }
                }

                count += 1;
            }
        }

        clock
    }
}
