const std = @import("std");
const mem = std.mem;

const kilo: usize = 1_000;
const mega: usize = 1_000_000;
const giga: usize = 1_000_000_000;

pub const ColorBand = enum {
    black,
    brown,
    red,
    orange,
    yellow,
    green,
    blue,
    violet,
    grey,
    white,
};

pub fn resistance(colors: []const ColorBand) usize {
    const c1 = @as(usize, @intFromEnum(colors[0]));
    const c2 = @as(usize, @intFromEnum(colors[1]));
    const c3 = @as(usize, @intFromEnum(colors[2]));

    return (c1 * 10 + c2) * std.math.pow(usize, 10, c3);
}

pub fn label(allocator: mem.Allocator, colors: []const ColorBand) mem.Allocator.Error![]u8 {
    const r = resistance(colors);

    var prefix: ?[]const u8 = null;
    var divisor: usize = 1;

    if (r >= giga) {
        prefix = "giga";
        divisor = giga;
    } else if (r >= mega) {
        prefix = "mega";
        divisor = mega;
    } else if (r >= kilo) {
        prefix = "kilo";
        divisor = kilo;
    }

    const v = @as(f64, @floatFromInt(r)) / @as(f64, @floatFromInt(divisor));

    if (prefix) |p| {
        return try std.fmt.allocPrint(allocator, "{d} {s}ohms", .{ v, p });
    } else {
        return try std.fmt.allocPrint(allocator, "{d} ohms", .{v});
    }
}
