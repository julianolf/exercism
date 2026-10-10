const std = @import("std");

pub const Relation = enum {
    equal,
    sublist,
    superlist,
    unequal,
};

pub fn compare(a: []const i32, b: []const i32) Relation {
    return switch (std.math.order(a.len, b.len)) {
        .eq => if (std.mem.eql(i32, a, b)) .equal else .unequal,
        .gt => if (contains(a, b)) .superlist else .unequal,
        .lt => if (contains(b, a)) .sublist else .unequal,
    };
}

fn contains(haystack: []const i32, needle: []const i32) bool {
    return std.mem.find(i32, haystack, needle) != null;
}
