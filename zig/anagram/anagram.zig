const std = @import("std");
const mem = std.mem;

/// Returns the set of strings in `candidates` that are anagrams of `word`.
/// Caller owns the returned memory.
pub fn detectAnagrams(
    allocator: mem.Allocator,
    word: []const u8,
    candidates: []const []const u8,
) !std.BufSet {
    var anagrams: std.BufSet = .init(allocator);
    errdefer anagrams.deinit();

    const word_count = countChars(word);
    for (candidates) |candidate| {
        if (candidate.len != word.len)
            continue;
        if (std.ascii.eqlIgnoreCase(candidate, word))
            continue;

        const candidate_count = countChars(candidate);
        if (std.mem.eql(u4, &candidate_count, &word_count))
            try anagrams.insert(candidate);
    }

    return anagrams;
}

fn countChars(word: []const u8) [26]u4 {
    var counter: [26]u4 = @splat(0);
    for (word) |c| {
        if (!std.ascii.isAlphabetic(c))
            continue;

        const index: usize = std.ascii.toLower(c) - 'a';
        counter[index] += 1;
    }
    return counter;
}
