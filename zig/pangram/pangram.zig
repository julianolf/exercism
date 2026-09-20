pub fn isPangram(str: []const u8) bool {
    const all_letters: u32 = (1 << 26) - 1;
    var seen: u32 = 0;

    for (str) |c| {
        const lower: u8 = switch (c) {
            'A'...'Z' => c | 0x20,
            'a'...'z' => c,
            else => continue,
        };
        seen |= @as(u32, 1) << @intCast(lower - 'a');
    }

    return seen == all_letters;
}
