const std = @import("std");

pub fn modifier(score: u8) i8 {
    return std.math.divFloor(i8, @as(i8, @intCast(score)) - 10, 2) catch unreachable;
}

pub fn ability(random: std.Random) u8 {
    var dices: [4]u8 = undefined;
    for (&dices) |*d| {
        d.* = random.uintLessThan(u8, 6) + 1;
    }
    std.mem.sort(u8, &dices, {}, std.sort.desc(u8));
    return dices[0] + dices[1] + dices[2];
}

pub fn hitpoints(constitution: u8) u8 {
    return @intCast(10 + modifier(constitution));
}

pub const Character = struct {
    strength: u8,
    dexterity: u8,
    constitution: u8,
    intelligence: u8,
    wisdom: u8,
    charisma: u8,
    hitpoints: u8,

    pub fn init(random: std.Random) Character {
        var c: Character = .{
            .strength = ability(random),
            .dexterity = ability(random),
            .constitution = ability(random),
            .intelligence = ability(random),
            .wisdom = ability(random),
            .charisma = ability(random),
            .hitpoints = undefined,
        };
        c.hitpoints = hitpoints(c.constitution);
        return c;
    }
};
