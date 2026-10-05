const std = @import("std");

pub const QueenError = error{
    InitializationFailure,
    InvalidAttack,
};

pub const Queen = struct {
    row: u3,
    col: u3,

    pub fn init(row: i8, col: i8) QueenError!Queen {
        return .{
            .row = std.math.cast(u3, row) orelse return QueenError.InitializationFailure,
            .col = std.math.cast(u3, col) orelse return QueenError.InitializationFailure,
        };
    }

    pub fn canAttack(self: Queen, other: Queen) QueenError!bool {
        if (self.row == other.row and self.col == other.col) return QueenError.InvalidAttack;
        const dr = @abs(@as(i8, self.row) - @as(i8, other.row));
        const dc = @abs(@as(i8, self.col) - @as(i8, other.col));
        return dr == 0 or dc == 0 or dr == dc;
    }
};
