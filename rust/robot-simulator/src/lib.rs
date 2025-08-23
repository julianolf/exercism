use std::str::FromStr;

#[derive(PartialEq, Debug)]
pub enum Direction {
    North,
    East,
    South,
    West,
}

pub enum Movement {
    Right,
    Left,
    Advance,
}

impl FromStr for Movement {
    type Err = InvalidMovement;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "R" => Ok(Movement::Right),
            "L" => Ok(Movement::Left),
            "A" => Ok(Movement::Advance),
            _ => Err(Self::Err {}),
        }
    }
}

pub struct InvalidMovement;

pub struct Position {
    x: i32,
    y: i32,
}

pub struct Robot {
    pos: Position,
    dir: Direction,
}

impl Robot {
    pub fn new(x: i32, y: i32, d: Direction) -> Self {
        Self {
            pos: Position { x, y },
            dir: d,
        }
    }

    #[must_use]
    pub fn turn_right(self) -> Self {
        match self.dir {
            Direction::North => Self {
                dir: Direction::East,
                ..self
            },
            Direction::South => Self {
                dir: Direction::West,
                ..self
            },
            Direction::East => Self {
                dir: Direction::South,
                ..self
            },
            Direction::West => Self {
                dir: Direction::North,
                ..self
            },
        }
    }

    #[must_use]
    pub fn turn_left(self) -> Self {
        match self.dir {
            Direction::North => Self {
                dir: Direction::West,
                ..self
            },
            Direction::South => Self {
                dir: Direction::East,
                ..self
            },
            Direction::East => Self {
                dir: Direction::North,
                ..self
            },
            Direction::West => Self {
                dir: Direction::South,
                ..self
            },
        }
    }

    #[must_use]
    pub fn advance(self) -> Self {
        match self.dir {
            Direction::North => Self {
                pos: Position {
                    y: self.pos.y + 1,
                    ..self.pos
                },
                ..self
            },
            Direction::South => Self {
                pos: Position {
                    y: self.pos.y - 1,
                    ..self.pos
                },
                ..self
            },
            Direction::East => Self {
                pos: Position {
                    x: self.pos.x + 1,
                    ..self.pos
                },
                ..self
            },
            Direction::West => Self {
                pos: Position {
                    x: self.pos.x - 1,
                    ..self.pos
                },
                ..self
            },
        }
    }

    #[must_use]
    pub fn instructions(self, instructions: &str) -> Self {
        let mut robot = Robot { ..self };

        for chr in instructions.split("") {
            match Movement::from_str(chr) {
                Ok(m) => match m {
                    Movement::Left => robot = robot.turn_left(),
                    Movement::Right => robot = robot.turn_right(),
                    Movement::Advance => robot = robot.advance(),
                },
                Err(_) => continue,
            }
        }

        robot
    }

    pub fn position(&self) -> (i32, i32) {
        let Position { x, y } = self.pos;
        (x, y)
    }

    pub fn direction(&self) -> &Direction {
        &self.dir
    }
}
