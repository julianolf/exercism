NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

directions = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def turn_right(self):
        self.direction = (self.direction + 90) % 360

    def turn_left(self):
        self.direction = (self.direction - 90) % 360

    def advance(self):
        x, y = directions[self.direction]
        self.x_pos += x
        self.y_pos += y

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
