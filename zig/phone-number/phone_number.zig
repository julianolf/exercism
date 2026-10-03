pub fn clean(phrase: []const u8) ?[10]u8 {
    var digits: [11]u8 = undefined;
    var len: usize = 0;

    for (phrase) |c| switch (c) {
        '0'...'9' => {
            if (len == digits.len) return null;
            digits[len] = c;
            len += 1;
        },
        ' ', '(', ')', '-', '.', '+' => continue,
        else => return null,
    };

    const number: *const [10]u8 = switch (len) {
        10 => digits[0..10],
        11 => if (digits[0] == '1') digits[1..11] else return null,
        else => return null,
    };

    if (number[0] < '2' or number[3] < '2') return null;
    return number.*;
}
