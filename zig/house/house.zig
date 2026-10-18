const std = @import("std");

pub const Error = error{InvalidVerse};

const verbs = [_][]const u8{
    "belonged to",
    "kept",
    "woke",
    "married",
    "kissed",
    "milked",
    "tossed",
    "worried",
    "killed",
    "ate",
    "lay in",
};

const subjects = [_][]const u8{
    "the horse and the hound and the horn",
    "the farmer sowing his corn",
    "the rooster that crowed in the morn",
    "the priest all shaven and shorn",
    "the man all tattered and torn",
    "the maiden all forlorn",
    "the cow with the crumpled horn",
    "the dog",
    "the cat",
    "the rat",
    "the malt",
    "the house that Jack built",
};

comptime {
    std.debug.assert(verbs.len + 1 == subjects.len);
}

pub fn recite(buffer: []u8, start_verse: u32, end_verse: u32) ![]const u8 {
    if (start_verse < 1 or start_verse > end_verse or end_verse > subjects.len)
        return Error.InvalidVerse;

    var w: std.Io.Writer = .fixed(buffer);

    for (start_verse..end_verse + 1) |verse_number| {
        if (verse_number != start_verse) try w.writeByte('\n');
        try writeVerse(&w, verse_number);
    }

    return w.buffered();
}

fn writeVerse(w: *std.Io.Writer, verse_number: usize) !void {
    const first = subjects.len - verse_number;
    try w.print("This is {s}", .{subjects[first]});

    for (verbs[first..], subjects[first + 1 ..]) |verb, subject| {
        try w.print(" that {s} {s}", .{ verb, subject });
    }

    try w.writeByte('.');
}
