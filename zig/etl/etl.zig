const std = @import("std");
const mem = std.mem;
const ascii = std.ascii;

pub fn transform(allocator: mem.Allocator, legacy: std.AutoHashMap(i5, []const u8)) mem.Allocator.Error!std.AutoHashMap(u8, i5) {
    var map: std.AutoHashMap(u8, i5) = .init(allocator);

    var it = legacy.iterator();
    while (it.next()) |entry| {
        const score = entry.key_ptr.*;
        const letters = entry.value_ptr.*;

        for (letters) |c| {
            try map.put(ascii.toLower(c), score);
        }
    }

    return map;
}
