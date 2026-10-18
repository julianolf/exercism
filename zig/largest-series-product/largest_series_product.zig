pub const SeriesError = error{
    InvalidCharacter,
    NegativeSpan,
    InsufficientDigits,
};

pub fn largestProduct(digits: []const u8, span: i32) SeriesError!u64 {
    if (span < 0) return SeriesError.NegativeSpan;

    const len: usize = @intCast(span);
    if (digits.len < len) return SeriesError.InsufficientDigits;

    for (digits) |c| if (c < '0' or c > '9') return SeriesError.InvalidCharacter;

    var largest: u64 = 0;
    for (0..digits.len - len + 1) |start| {
        var product: u64 = 1;
        for (digits[start..][0..len]) |c| product *= c - '0';
        largest = @max(product, largest);
    }

    return largest;
}
