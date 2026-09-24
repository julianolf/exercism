pub const HighScores = struct {
    scores: []const i32,
    top: [3]i32,

    pub fn init(scores: []const i32) HighScores {
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

        return .{ .scores = scores, .top = top };
    }

    pub fn latest(self: *const HighScores) ?i32 {
        if (self.scores.len == 0)
            return null;

        return self.scores[self.scores.len - 1];
    }

    pub fn personalBest(self: *const HighScores) ?i32 {
        if (self.scores.len == 0)
            return null;

        var best: i32 = 0;
        for (self.scores) |score| {
            if (score > best)
                best = score;
        }

        return best;
    }

    pub fn personalTopThree(self: *const HighScores) []const i32 {
        const n: usize = @min(3, self.scores.len);
        return self.top[0..n];
    }
};
