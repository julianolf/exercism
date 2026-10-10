const std = @import("std");

pub fn primes(buffer: []u32, limit: u12) []u32 {
    if (limit < 2) return buffer[0..0];

    buffer[0] = 2;

    var i: usize = 1;
    var n: u32 = 3;
    search: while (n <= limit and i < buffer.len) : (n += 2) {
        for (buffer[0..i]) |p| if (n % p == 0) continue :search;

        buffer[i] = n;
        i += 1;
    }

    return buffer[0..i];
}
