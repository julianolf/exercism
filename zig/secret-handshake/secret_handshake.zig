const std = @import("std");
const mem = std.mem;

pub const Signal = enum {
    wink,
    double_blink,
    close_your_eyes,
    jump,
};

pub fn calculateHandshake(allocator: mem.Allocator, number: u5) mem.Allocator.Error![]const Signal {
    const signals: std.EnumSet(Signal) = .{ .bits = .{ .mask = @truncate(number) } };
    var handshake = try allocator.alloc(Signal, signals.count());

    var index: usize = 0;
    var it = signals.iterator();
    while (it.next()) |signal| : (index += 1) {
        handshake[index] = signal;
    }

    if (number & 0b10000 != 0) mem.reverse(Signal, handshake);

    return handshake;
}
