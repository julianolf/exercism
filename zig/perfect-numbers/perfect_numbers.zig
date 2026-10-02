const std = @import("std");

pub const Classification = enum {
    deficient,
    perfect,
    abundant,
};

pub fn classify(n: u64) Classification {
    std.debug.assert(n != 0);

    var sum: u128 = if (n == 1) 0 else 1;
    const n_sqrt = std.math.sqrt(n);
    var d: u64 = 2;
    while (d <= n_sqrt) : (d += 1) {
        if (n % d != 0) continue;
        sum += d;
        const r = n / d;
        if (r != d) sum += r;
        if (sum > n) return .abundant;
    }

    return switch (std.math.order(sum, n)) {
        .lt => .deficient,
        .eq => .perfect,
        .gt => .abundant,
    };
}
