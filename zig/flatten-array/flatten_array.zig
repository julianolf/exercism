const std = @import("std");
const mem = std.mem;

pub const Box = union(enum) {
    none,
    one: i12,
    many: []const Box,
};

pub fn flatten(allocator: mem.Allocator, box: Box) mem.Allocator.Error![]i12 {
    const arr = try allocator.alloc(i12, count(box));
    var i: usize = 0;
    fill(arr, &i, box);
    return arr;
}

fn count(box: Box) usize {
    return switch (box) {
        .none => 0,
        .one => 1,
        .many => |boxes| blk: {
            var n: usize = 0;
            for (boxes) |b| n += count(b);
            break :blk n;
        },
    };
}

fn fill(arr: []i12, i: *usize, box: Box) void {
    switch (box) {
        .none => {},
        .one => |value| {
            arr[i.*] = value;
            i.* += 1;
        },
        .many => |boxes| for (boxes) |b| fill(arr, i, b),
    }
}
