const std = @import("std");
const mem = std.mem;
const ascii = std.ascii;

const group_size: usize = 5;

/// Encodes `s` using the Atbash cipher. Caller owns the returned memory.
pub fn encode(allocator: mem.Allocator, s: []const u8) mem.Allocator.Error![]u8 {
    var out: std.ArrayList(u8) = try .initCapacity(allocator, s.len + s.len / group_size);
    errdefer out.deinit(allocator);

    var counter: usize = 0;
    for (s) |c| {
        const char = transpose(c) orelse continue;
        if (counter > 0 and counter % group_size == 0) out.appendAssumeCapacity(' ');
        out.appendAssumeCapacity(char);
        counter += 1;
    }

    return out.toOwnedSlice(allocator);
}

/// Decodes `s` using the Atbash cipher. Caller owns the returned memory.
pub fn decode(allocator: mem.Allocator, s: []const u8) mem.Allocator.Error![]u8 {
    var out: std.ArrayList(u8) = try .initCapacity(allocator, s.len);
    errdefer out.deinit(allocator);

    for (s) |c| {
        if (transpose(c)) |char| out.appendAssumeCapacity(char);
    }

    return out.toOwnedSlice(allocator);
}

fn transpose(c: u8) ?u8 {
    return switch (c) {
        'a'...'z', 'A'...'Z' => 'z' - (ascii.toLower(c) - 'a'),
        '0'...'9' => c,
        else => null,
    };
}
