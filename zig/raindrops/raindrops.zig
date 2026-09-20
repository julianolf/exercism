const std = @import("std");

pub fn convert(buffer: []u8, n: u32) []const u8 {
    var w = std.Io.Writer.fixed(buffer);

    if (n % 3 == 0) w.writeAll("Pling") catch unreachable;
    if (n % 5 == 0) w.writeAll("Plang") catch unreachable;
    if (n % 7 == 0) w.writeAll("Plong") catch unreachable;
    if (w.end == 0) w.print("{d}", .{n}) catch unreachable;

    return buffer[0..w.end];
}
