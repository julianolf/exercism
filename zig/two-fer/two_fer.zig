const std = @import("std");

pub fn twoFer(buffer: []u8, name: ?[]const u8) ![]u8 {
    var w: std.Io.Writer = .fixed(buffer);
    try w.print("One for {s}, one for me.", .{name orelse "you"});
    return w.buffered();
}
