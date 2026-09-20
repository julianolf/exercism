pub fn isIsogram(str: []const u8) bool {
    var flag: u32 = 0;
    var mask: u32 = 0;

    for (str) |c| {
        mask = switch (c) {
            'A'...'Z' => @as(u32, 1) << @intCast(c - 'A'),
            'a'...'z' => @as(u32, 1) << @intCast(c - 'a'),
            else => continue,
        };

        if (flag & mask != 0) return false;

        flag |= mask;
    }

    return true;
}
