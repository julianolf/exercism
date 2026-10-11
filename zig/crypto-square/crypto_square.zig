const std = @import("std");
const mem = std.mem;

const RectSize = struct {
    col: usize,
    row: usize,
};

/// Encodes `plaintext` using the square code. Caller owns the returned memory.
pub fn ciphertext(allocator: mem.Allocator, plaintext: []const u8) mem.Allocator.Error![]u8 {
    const buf = try allocator.alloc(u8, plaintext.len);
    defer allocator.free(buf);
    const normalized = normalize(buf, plaintext);

    if (normalized.len == 0) return allocator.alloc(u8, 0);

    const size = calcRectSize(normalized.len);
    const out = try allocator.alloc(u8, size.col * size.row + size.col - 1);

    var k: usize = 0;
    for (0..size.col) |c| {
        if (c > 0) {
            out[k] = ' ';
            k += 1;
        }
        for (0..size.row) |r| {
            const i = r * size.col + c;
            out[k] = if (i < normalized.len) normalized[i] else ' ';
            k += 1;
        }
    }

    return out;
}

fn normalize(buf: []u8, s: []const u8) []u8 {
    var n: usize = 0;
    for (s) |c| {
        if (!std.ascii.isAlphanumeric(c)) continue;
        buf[n] = std.ascii.toLower(c);
        n += 1;
    }

    return buf[0..n];
}

fn calcRectSize(len: usize) RectSize {
    var col: usize = std.math.sqrt(len);
    if (col * col < len) col += 1;
    return .{ .col = col, .row = (len + col - 1) / col };
}
