const std = @import("std");
const mem = std.mem;

/// Returns the set of strings in `candidates` that are anagrams of `word`.
/// Caller owns the returned memory.
pub fn detectAnagrams(
    allocator: mem.Allocator,
    word: []const u8,
    candidates: []const []const u8,
) !std.BufSet {
    var char_map: std.AutoHashMap(u8, u4) = .init(allocator);
    defer char_map.deinit();

    for (word) |c| {
        if (!std.ascii.isAlphabetic(c))
            continue;

        const key = std.ascii.toLower(c);
        const entry = try char_map.getOrPutValue(key, 0);
        entry.value_ptr.* += 1;
    }

    var anagrams: std.BufSet = .init(allocator);
    errdefer anagrams.deinit();

    outer: for (candidates) |candidate| {
        if (candidate.len != word.len) continue;
        if (std.ascii.eqlIgnoreCase(candidate, word)) continue;

        var clone = try char_map.clone();
        defer clone.deinit();

        for (candidate) |c| {
            if (!std.ascii.isAlphabetic(c))
                continue;

            const key = std.ascii.toLower(c);
            if (!clone.contains(key))
                continue :outer;

            const value = clone.getPtr(key);
            if (value) |v| {
                if (v.* == 0)
                    continue :outer;
                v.* -= 1;
            }
        }

        var it = clone.valueIterator();
        while (it.next()) |v| {
            if (v.* != 0)
                continue :outer;
        }

        try anagrams.insert(candidate);
    }

    return anagrams;
}
