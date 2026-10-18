pub fn isValid(s: []const u8) bool {
    var sum: u8 = 0;
    var digits: usize = 0;
    var double: bool = false;
    var i: usize = s.len;
    while (i > 0) {
        i -= 1;
        switch (s[i]) {
            '0'...'9' => |c| {
                var d = c - '0';
                if (double) {
                    d *= 2;
                    if (d > 9) d -= 9;
                }
                sum = (sum + d) % 10;
                double = !double;
                digits += 1;
            },
            ' ' => {},
            else => return false,
        }
    }
    return digits > 1 and sum == 0;
}
