use core::ops::Not;
use std::collections::HashMap;
use std::fmt;
use std::str::FromStr;

struct InvalidResult;

#[derive(Copy, Clone)]
enum MatchResult {
    Loss = 0,
    Draw = 1,
    Win = 3,
}

impl FromStr for MatchResult {
    type Err = InvalidResult;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "loss" => Ok(MatchResult::Loss),
            "draw" => Ok(MatchResult::Draw),
            "win" => Ok(MatchResult::Win),
            _ => Err(InvalidResult {}),
        }
    }
}

impl Not for MatchResult {
    type Output = Self;

    fn not(self) -> Self::Output {
        match self {
            MatchResult::Loss => MatchResult::Win,
            MatchResult::Draw => MatchResult::Draw,
            MatchResult::Win => MatchResult::Loss,
        }
    }
}

#[derive(Eq, Ord, PartialEq, PartialOrd)]
struct Team {
    name: String,
    matches: u32,
    wins: u32,
    draws: u32,
    losses: u32,
    points: u32,
}

impl Team {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            matches: 0,
            wins: 0,
            draws: 0,
            losses: 0,
            points: 0,
        }
    }

    fn update(&mut self, result: &MatchResult) {
        self.matches += 1;
        self.points += *result as u32;

        match result {
            MatchResult::Loss => self.losses += 1,
            MatchResult::Draw => self.draws += 1,
            MatchResult::Win => self.wins += 1,
        }
    }
}

struct Tournament<'a> {
    teams: HashMap<&'a str, Team>,
}

impl fmt::Display for Tournament<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:<30} | MP |  W |  D |  L |  P", "Team")?;

        let mut teams: Vec<&Team> = self.teams.values().collect();

        // There might be a better way for sorting
        teams.sort_by(|a, b| a.name.cmp(&b.name));
        teams.sort_by(|a, b| b.points.cmp(&a.points));

        for team in teams {
            write!(
                f,
                "\n{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}",
                team.name, team.matches, team.wins, team.draws, team.losses, team.points
            )?;
        }

        write!(f, "")
    }
}

pub fn tally(match_results: &str) -> String {
    let mut data: HashMap<&str, Team> = HashMap::new();

    for line in match_results
        .lines()
        .map(|l| l.split(';').collect::<Vec<&str>>())
    {
        match line[..] {
            [first, second, result] => match MatchResult::from_str(result) {
                Ok(r) => {
                    let first_team = data.entry(first).or_insert_with(|| Team::new(first));
                    first_team.update(&r);

                    let second_team = data.entry(second).or_insert_with(|| Team::new(second));
                    second_team.update(&!r);
                }
                Err(_) => continue,
            },
            _ => continue,
        }
    }

    let tournament = Tournament { teams: data };

    format!("{}", tournament)
}
