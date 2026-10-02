const std = @import("std");

pub fn truncate(phrase: []const u8) []const u8 {
    var utf8 = std.unicode.Utf8View.initUnchecked(phrase).iterator();
    return utf8.peek(5);
}
