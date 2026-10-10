const std = @import("std");

pub fn primes(buffer: []u32, comptime limit: u32) []u32 {
    var composite: std.StaticBitSet(@as(usize, limit) + 1) = .empty;

    var count: usize = 0;
    var n: usize = 2;
    while (n <= limit) : (n += 1) {
        if (composite.isSet(n)) continue;

        buffer[count] = @intCast(n);
        count += 1;

        var m = n * n;
        while (m <= limit) : (m += n) composite.set(m);
    }

    return buffer[0..count];
}
