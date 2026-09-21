const std = @import("std");
const mem = std.mem;
const ascii = std.ascii;

pub fn abbreviate(allocator: mem.Allocator, words: []const u8) mem.Allocator.Error![]u8 {
    var letters: std.ArrayList(u8) = .empty;
    defer letters.deinit(allocator);

    var iter = mem.tokenizeAny(u8, words, " -");
    while (iter.next()) |word| {
        for (word) |c| {
            if (!ascii.isAlphabetic(c))
                continue;
            try letters.append(allocator, ascii.toUpper(c));
            break;
        }
    }

    return letters.toOwnedSlice(allocator);
}
