const std = @import("std");
const mem = std.mem;

pub const ConversionError = error{
    InvalidInputBase,
    InvalidOutputBase,
    InvalidDigit,
};

/// Converts `digits` from `input_base` to `output_base`, returning a slice of digits.
/// Caller owns the returned memory.
pub fn convert(
    allocator: mem.Allocator,
    digits: []const u32,
    input_base: u32,
    output_base: u32,
) (mem.Allocator.Error || ConversionError)![]u32 {
    if (input_base < 2) return ConversionError.InvalidInputBase;
    if (output_base < 2) return ConversionError.InvalidOutputBase;

    var value: u32 = 0;
    for (digits) |d| {
        if (d >= input_base) return ConversionError.InvalidDigit;
        value = value * input_base + d; // Horner's method
    }

    var out: std.ArrayList(u32) = .empty;
    errdefer out.deinit(allocator);

    while (true) {
        try out.append(allocator, value % output_base);
        value /= output_base;
        if (value == 0) break;
    }
    mem.reverse(u32, out.items);

    return out.toOwnedSlice(allocator);
}
