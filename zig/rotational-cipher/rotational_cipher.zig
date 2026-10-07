const std = @import("std");
const mem = std.mem;

pub fn rotate(allocator: mem.Allocator, text: []const u8, shiftKey: u5) mem.Allocator.Error![]u8 {
    const enc = try allocator.alloc(u8, text.len);
    for (text, enc) |c, *e| {
        e.* = switch (c) {
            'a'...'z' => (c - 'a' + shiftKey) % 26 + 'a',
            'A'...'Z' => (c - 'A' + shiftKey) % 26 + 'A',
            else => c,
        };
    }
    return enc;
}
