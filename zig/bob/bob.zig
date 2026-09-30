const std = @import("std");

const sure = "Sure.";
const fine = "Fine. Be that way!";
const chill = "Whoa, chill out!";
const whatever = "Whatever.";
const calm_down = "Calm down, I know what I'm doing!";

const Flags = packed struct {
    upper: bool = false,
    lower: bool = false,
    q_mark: bool = false,
};

pub fn response(s: []const u8) []const u8 {
    const str = std.mem.trim(u8, s, &std.ascii.whitespace);

    if (str.len == 0) return fine;

    var flags: Flags = .{ .q_mark = (str[str.len - 1] == '?') };
    for (str) |c| {
        if (std.ascii.isLower(c)) flags.lower = true;
        if (std.ascii.isUpper(c)) flags.upper = true;
    }

    const f: u3 = @bitCast(flags);
    switch (f) {
        0b101 => return calm_down,
        0b001 => return chill,
        0b100, 0b110, 0b111 => return sure,
        else => return whatever,
    }
}
