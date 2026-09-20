/// Writes a reversed copy of `s` to `buffer`.
pub fn reverse(buffer: []u8, s: []const u8) []u8 {
    var i: usize = 0;
    var j: usize = s.len;

    while (i < s.len) : ({
        i += 1;
        j -= 1;
    }) {
        buffer[i] = s[j - 1];
    }

    return buffer[0..s.len];
}
