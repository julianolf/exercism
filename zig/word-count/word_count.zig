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

        const res = try count.getOrPutAdapted(token, CaseInsensitiveContext{});
        if (res.found_existing) {
            res.value_ptr.* += 1;
            continue;
        }
        errdefer count.removeByPtr(res.key_ptr);
        res.key_ptr.* = try ascii.allocLowerString(allocator, token);
        res.value_ptr.* = 1;
    }

    return count;
}

fn isWordChar(c: u8) bool {
    return ascii.isAlphanumeric(c) or c == '\'';
}

const CaseInsensitiveContext = struct {
    pub fn hash(_: CaseInsensitiveContext, key: []const u8) u64 {
        var hasher: std.hash.Wyhash = .init(0);
        var buf: [64]u8 = undefined;
        var res = key;
        while (res.len > 0) {
            const n = @min(res.len, buf.len);
            hasher.update(ascii.lowerString(&buf, res[0..n]));
            res = res[n..];
        }
        return hasher.final();
    }

    pub fn eql(_: CaseInsensitiveContext, token: []const u8, stored: []const u8) bool {
        return ascii.eqlIgnoreCase(token, stored);
    }
};
