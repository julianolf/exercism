const std = @import("std");
const mem = std.mem;

pub fn factors(allocator: mem.Allocator, value: u64) mem.Allocator.Error![]u64 {
    var f: std.ArrayList(u64) = .empty;
    defer f.deinit(allocator);

    var r: u64 = value;
    while (r % 2 == 0 and r > 1) {
        try f.append(allocator, 2);
        r /= 2;
    }

    var d: u64 = 3;
    while (d <= r / d) : (d += 2) {
        while (r % d == 0) {
            try f.append(allocator, d);
            r /= d;
        }
    }

    if (r > 1) try f.append(allocator, r);

    return try f.toOwnedSlice(allocator);
}
