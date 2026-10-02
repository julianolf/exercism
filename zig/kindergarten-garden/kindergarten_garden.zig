const std = @import("std");

pub const Plant = enum {
    clover,
    grass,
    radishes,
    violets,

    pub fn fromChar(c: u8) Plant {
        return switch (c) {
            'C' => Plant.clover,
            'G' => Plant.grass,
            'R' => Plant.radishes,
            'V' => Plant.violets,
            else => unreachable,
        };
    }
};

pub fn plants(diagram: []const u8, student: []const u8) [4]Plant {
    var result: [4]Plant = undefined;

    const cup: usize = (student[0] - 'A') * 2; // 2 cups per row per student
    var row: usize = 0;
    var lines = std.mem.tokenizeScalar(u8, diagram, '\n');
    while (lines.next()) |line| : (row += 1) {
        result[row * 2] = Plant.fromChar(line[cup]);
        result[row * 2 + 1] = Plant.fromChar(line[cup + 1]);
    }

    return result;
}
