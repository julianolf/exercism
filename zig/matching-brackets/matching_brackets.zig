const std = @import("std");
const mem = std.mem;

pub const Error = error{NestingTooDeep};

const max_depth: usize = 10;

pub fn isBalanced(_: mem.Allocator, s: []const u8) !bool {
    var expected: [max_depth]u8 = undefined;
    var depth: usize = 0;

    for (s) |c| switch (c) {
        '{', '[', '(' => {
            if (depth == max_depth) return Error.NestingTooDeep;
            expected[depth] = closerOf(c);
            depth += 1;
        },
        '}', ']', ')' => {
            if (depth == 0 or expected[depth - 1] != c) return false;
            depth -= 1;
        },
        else => {},
    };

    return depth == 0;
}

fn closerOf(open: u8) u8 {
    return switch (open) {
        '{' => '}',
        '[' => ']',
        '(' => ')',
        else => unreachable,
    };
}
