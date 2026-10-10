const std = @import("std");

pub const LyricsError = error{InvalidVerse};

const ordinals = [_][]const u8{
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
};

const gifts = [_][]const u8{
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
};

comptime {
    std.debug.assert(ordinals.len == gifts.len);
}

pub fn recite(buffer: []u8, start_verse: u32, end_verse: u32) (LyricsError || std.Io.Writer.Error)![]const u8 {
    if (start_verse < 1 or end_verse > gifts.len or start_verse > end_verse)
        return LyricsError.InvalidVerse;

    var w: std.Io.Writer = .fixed(buffer);

    for (start_verse..end_verse + 1) |verse| {
        if (verse != start_verse) try w.writeByte('\n');

        try w.print("On the {s} day of Christmas my true love gave to me: ", .{ordinals[verse - 1]});

        var gift = verse;
        while (gift > 1) : (gift -= 1) {
            try w.print("{s}, ", .{gifts[gift - 1]});
        }
        if (verse > 1) try w.writeAll("and ");
        try w.print("{s}.", .{gifts[0]});
    }

    return w.buffered();
}
