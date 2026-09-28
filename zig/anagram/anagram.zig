const std = @import("std");
const mem = std.mem;

/// Returns the set of strings in `candidates` that are anagrams of `word`.
/// Caller owns the returned memory.
pub fn detectAnagrams(
    allocator: mem.Allocator,
    word: []const u8,
    candidates: []const []const u8,
) !std.BufSet {
    const sorted_word = try std.ascii.allocLowerString(allocator, word);
    defer allocator.free(sorted_word);
    std.mem.sort(u8, sorted_word, {}, std.sort.asc(u8));

    var anagrams: std.BufSet = .init(allocator);
    errdefer anagrams.deinit();

    for (candidates) |candidate| {
        if (candidate.len != word.len)
            continue;
        if (std.ascii.eqlIgnoreCase(candidate, word))
            continue;

        const sorted_candidate = try std.ascii.allocLowerString(allocator, candidate);
        defer allocator.free(sorted_candidate);
        std.mem.sort(u8, sorted_candidate, {}, std.sort.asc(u8));

        if (std.mem.eql(u8, sorted_candidate, sorted_word))
            try anagrams.insert(candidate);
    }

    return anagrams;
}
