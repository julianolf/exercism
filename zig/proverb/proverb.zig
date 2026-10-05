const std = @import("std");
const mem = std.mem;
const fmt = std.fmt;

pub fn recite(allocator: mem.Allocator, words: []const []const u8) mem.Allocator.Error![][]u8 {
    var proverb: std.ArrayList([]u8) = try .initCapacity(allocator, words.len);
    errdefer {
        for (proverb.items) |item| allocator.free(item);
        proverb.deinit(allocator);
    }

    if (words.len == 0) return proverb.toOwnedSlice(allocator);

    for (words[0 .. words.len - 1], words[1..]) |want, lost| {
        const rhyme = try fmt.allocPrint(allocator, "For want of a {s} the {s} was lost.\n", .{ want, lost });
        proverb.appendAssumeCapacity(rhyme);
    }
    const rhyme = try fmt.allocPrint(allocator, "And all for the want of a {s}.\n", .{words[0]});
    proverb.appendAssumeCapacity(rhyme);

    return proverb.toOwnedSlice(allocator);
}
