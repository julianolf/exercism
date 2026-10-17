const std = @import("std");
const mem = std.mem;

pub fn rows(allocator: mem.Allocator, letter: u8) mem.Allocator.Error![][]u8 {
    std.debug.assert(letter >= 'A' and letter <= 'Z');

    const half: usize = letter - 'A';
    const size: usize = 2 * half + 1;
    const matrix = try alloc(allocator, size);

    for (matrix, 0..) |row, i| {
        const n = if (i <= half) i else size - 1 - i;
        const c: u8 = @intCast('A' + n);
        row[half - n] = c;
        row[half + n] = c;
    }

    return matrix;
}

fn alloc(allocator: mem.Allocator, size: usize) mem.Allocator.Error![][]u8 {
    const m = try allocator.alloc([]u8, size);
    errdefer allocator.free(m);

    var i: usize = 0;
    errdefer for (m[0..i]) |r| allocator.free(r);

    while (i < size) : (i += 1) {
        m[i] = try allocator.alloc(u8, size);
        @memset(m[i], ' ');
    }

    return m;
}
