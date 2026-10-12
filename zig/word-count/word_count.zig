const std = @import("std");
const mem = std.mem;
const ascii = std.ascii;

/// Returns the counts of the words in `s`.
/// Caller owns the returned memory.
pub fn countWords(allocator: mem.Allocator, s: []const u8) !std.StringHashMap(u32) {
    var count: std.StringHashMap(u32) = .init(allocator);
    errdefer {
        var it = count.keyIterator();
        while (it.next()) |k| allocator.free(k.*);
        count.deinit();
    }

    var i: usize = 0;
    while (i < s.len) {
        while (i < s.len and !isWordChar(s[i])) i += 1;
        const start = i;
        while (i < s.len and isWordChar(s[i])) i += 1;

        const token = mem.trim(u8, s[start..i], "'");
        if (token.len == 0) continue;

        const word = try ascii.allocLowerString(allocator, token);
        errdefer allocator.free(word);

        const res = try count.getOrPut(word);
        if (res.found_existing) {
            allocator.free(word);
            res.value_ptr.* += 1;
        } else {
            res.value_ptr.* = 1;
        }
    }

    return count;
}

fn isWordChar(c: u8) bool {
    return ascii.isAlphanumeric(c) or c == '\'';
}
