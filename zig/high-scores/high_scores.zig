pub const HighScores = struct {
    latest_: ?i32 = null,
    best: ?i32 = null,
    top: [3]i32 = undefined,
    len: usize = 0,

    pub fn init(scores: []const i32) HighScores {
        if (scores.len == 0)
            return .{};

        var top: [3]i32 = @splat(0);

        for (scores) |score| {
            if (score > top[0]) {
                top[2] = top[1];
                top[1] = top[0];
                top[0] = score;
            } else if (score > top[1]) {
                top[2] = top[1];
                top[1] = score;
            } else if (score > top[2]) {
                top[2] = score;
            }
        }

        return .{
            .latest_ = scores[scores.len - 1],
            .best = top[0],
            .top = top,
            .len = @min(3, scores.len),
        };
    }

    pub fn latest(self: *const HighScores) ?i32 {
        return self.latest_;
    }

    pub fn personalBest(self: *const HighScores) ?i32 {
        return self.best;
    }

    pub fn personalTopThree(self: *const HighScores) []const i32 {
        return self.top[0..self.len];
    }
};
