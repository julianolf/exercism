const inner: f32 = 1 * 1;
const middle: f32 = 5 * 5;
const outer: f32 = 10 * 10;

pub const Coordinate = struct {
    x: f32,
    y: f32,

    pub fn init(x_coord: f32, y_coord: f32) Coordinate {
        return .{ .x = x_coord, .y = y_coord };
    }

    pub fn score(self: Coordinate) usize {
        const v = (self.x * self.x) + (self.y * self.y);
        if (v <= inner) return 10;
        if (v <= middle) return 5;
        if (v <= outer) return 1;
        return 0;
    }
};
