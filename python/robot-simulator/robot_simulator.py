NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def turn_right(self):
        self.direction = (self.direction + 1) % 5 or 1

    def turn_left(self):
        self.direction = self.direction - 1 or 4

    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        elif self.direction == WEST:
            self.x_pos -= 1
        else:
            raise ValueError(f"Unknown direction {self.direction}")

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()
            else:
                raise ValueError(f"Unknown instruction {instruction}")
