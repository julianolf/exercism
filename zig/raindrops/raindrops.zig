const std = @import("std");

pub fn convert(buffer: []u8, n: u32) []const u8 {
    const pling = n % 3 == 0;
    const plang = n % 5 == 0;
    const plong = n % 7 == 0;

    var w = std.Io.Writer.fixed(buffer);

    if (pling) w.writeAll("Pling") catch {};
    if (plang) w.writeAll("Plang") catch {};
    if (plong) w.writeAll("Plong") catch {};
    if (!pling and !plang and !plong) w.print("{d}", .{n}) catch {};

    return buffer[0..w.end];
}
