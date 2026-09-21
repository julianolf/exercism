const std = @import("std");
const mem = std.mem;

pub fn sum(allocator: mem.Allocator, factors: []const u32, limit: u32) !u64 {
    _ = allocator; // I suppose this was intended for a hash map
    var result: u64 = 0;
    var seen: bool = false;

    for (1..limit) |number| {
        seen = false;
        for (factors) |factor| {
            if (factor == 0) continue;
            if ((number % factor == 0) and !seen) {
                result += number;
                seen = true;
            }
        }
    }

    return result;
}
