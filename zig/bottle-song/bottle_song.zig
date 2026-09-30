const std = @import("std");

const numbers = [_][]const u8{
    "No",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
};

const verse =
    \\{s} green bottle{s} hanging on the wall,
    \\{s} green bottle{s} hanging on the wall,
    \\And if one green bottle should accidentally fall,
    \\There'll be {s} green bottle{s} hanging on the wall.{s}
;

pub fn recite(buffer: []u8, start_bottles: u32, take_down: u32) ![]const u8 {
    var w: std.Io.Writer = .fixed(buffer);

    var i: usize = start_bottles;
    var t: usize = take_down;

    while (t > 0) : ({
        i -= 1;
        t -= 1;
    }) {
        var b: [5:0]u8 = undefined;

        const n1 = numbers[i];
        const n2 = std.ascii.lowerString(&b, numbers[i - 1]);
        const b1 = if (i != 1) "s" else "";
        const b2 = if (i - 1 != 1) "s" else "";
        const lf = if (t > 1) "\n\n" else "";
        const args = .{ n1, b1, n1, b1, n2, b2, lf };

        try w.print(verse, args);
    }

    return w.buffered();
}
