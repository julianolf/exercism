pub const Planet = enum {
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune,

    pub fn age(self: Planet, seconds: usize) f64 {
        const earth_age = @as(f64, @floatFromInt(seconds)) / 31_557_600;
        return switch (self) {
            .mercury => earth_age / 0.2408467,
            .venus => earth_age / 0.61519726,
            .earth => earth_age / 1.0,
            .mars => earth_age / 1.8808158,
            .jupiter => earth_age / 11.862615,
            .saturn => earth_age / 29.447498,
            .uranus => earth_age / 84.016846,
            .neptune => earth_age / 164.79132,
        };
    }
};
