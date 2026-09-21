const std = @import("std");
const mem = std.mem;

pub fn sum(allocator: mem.Allocator, factors: []const u32, limit: u32) !u64 {
    var map: std.hash_map.AutoHashMap(u32, void) = .init(allocator);
    defer map.deinit();

    for (factors) |f| {
        if (f == 0) continue;
        var i = f;
        while (i < limit) : (i += f) {
            try map.put(i, {});
        }
    }

    var result: u64 = 0;
    var iter = map.keyIterator();
    while (iter.next()) |k| {
        result += k.*;
    }

    return result;
}
