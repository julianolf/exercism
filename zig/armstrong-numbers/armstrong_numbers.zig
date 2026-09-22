const std = @import("std");

pub fn isArmstrongNumber(num: u128) bool {
    if (num == 0)
        return true;

    const n_digits: u128 = std.math.log10_int(num) + 1;
    var sum: u128 = 0;

    var n = num;
    while (n > 0) : (n /= 10) {
        const digit = n % 10;
        sum += std.math.pow(u128, digit, n_digits);
    }

    return (sum == num);
}
