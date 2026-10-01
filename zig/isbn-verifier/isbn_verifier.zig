const std = @import("std");

pub fn isValidIsbn10(s: []const u8) bool {
    if (s.len != 10 and s.len != 13) return false;
    if (!std.ascii.isDigit(s[0])) return false;
    if (!std.ascii.isDigit(s[s.len - 1]) and s[s.len - 1] != 'X') return false;

    var sum: usize = 0;
    var weight: u4 = 10;
    for (s) |c| {
        if (weight == 0) return false;
        const d = switch (c) {
            '-' => continue,
            '0'...'9' => c - '0',
            'X' => if (weight == 1) 10 else return false,
            else => return false,
        };
        sum += d * weight;
        weight -= 1;
    }

    return weight == 0 and sum % 11 == 0;
}
