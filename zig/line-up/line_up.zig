const std = @import("std");
const mem = std.mem;

fn ordinalSuffix(n: u10) []const u8 {
    const mod100 = n % 100;
    if (mod100 >= 11 and mod100 <= 13)
        return "th";

    return switch (n % 10) {
        1 => "st",
        2 => "nd",
        3 => "rd",
        else => "th",
    };
}

pub fn format(allocator: mem.Allocator, name: []const u8, number: u10) ![]u8 {
    const fmt = "{s}, you are the {d}{s} customer we serve today. Thank you!";
    const suffix = ordinalSuffix(number);
    return try std.fmt.allocPrint(allocator, fmt, .{ name, number, suffix });
}
