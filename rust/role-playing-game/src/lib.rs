pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        match self.health {
            0 => Some(Player {
                health: 100,
                level: self.level,
                mana: if self.level < 10 { None } else { Some(100) },
            }),
            _ => None,
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if self.level < 10 {
            self.health = if self.health >= mana_cost {
                self.health - mana_cost
            } else {
                0
            };

            return 0;
        }

        match self.mana {
            Some(mana) if mana >= mana_cost => {
                self.mana = Some(mana - mana_cost);

                mana_cost * 2
            }
            Some(_) => 0,
            None => 0,
        }
    }
}
