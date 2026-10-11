const std = @import("std");

const minutes_per_day = 24 * 60;

pub const Clock = struct {
    minutes: u16,

    /// Initializes a Clock, normalizing the given hour and minute.
    pub fn init(hour: i32, minute: i32) Clock {
        return fromMinutes(@as(i64, hour) * 60 + minute);
    }

    /// Moves the clock forwards by `minutes` minutes.
    pub fn advance(self: *Clock, minutes: i32) void {
        self.* = fromMinutes(@as(i64, self.minutes) + minutes);
    }

    /// Moves the clock backwards by `minutes` minutes.
    pub fn rewind(self: *Clock, minutes: i32) void {
        self.* = fromMinutes(@as(i64, self.minutes) - minutes);
    }

    /// Renders the time as "hh:mm".
    pub fn toString(self: Clock) [5]u8 {
        const hh = std.fmt.digits2(@intCast(self.minutes / 60));
        const mm = std.fmt.digits2(@intCast(self.minutes % 60));
        return .{ hh[0], hh[1], ':', mm[0], mm[1] };
    }

    /// Returns whether two clocks show the same time.
    pub fn eql(self: Clock, other: Clock) bool {
        return self.minutes == other.minutes;
    }

    fn fromMinutes(minutes: i64) Clock {
        return .{ .minutes = @intCast(@mod(minutes, minutes_per_day)) };
    }
};
