const std = @import("std");
const mem = std.mem;

pub const TranslationError = error{
    InvalidCodon,
};

pub const Protein = enum {
    methionine,
    phenylalanine,
    leucine,
    serine,
    tyrosine,
    cysteine,
    tryptophan,

    /// Codon -> amino acid. `null` value marks a STOP codon.
    const codon_table: std.StaticStringMap(?Protein) = .initComptime(.{
        .{ "AUG", .methionine },
        .{ "UUU", .phenylalanine },
        .{ "UUC", .phenylalanine },
        .{ "UUA", .leucine },
        .{ "UUG", .leucine },
        .{ "UCU", .serine },
        .{ "UCC", .serine },
        .{ "UCA", .serine },
        .{ "UCG", .serine },
        .{ "UAU", .tyrosine },
        .{ "UAC", .tyrosine },
        .{ "UGU", .cysteine },
        .{ "UGC", .cysteine },
        .{ "UGG", .tryptophan },
        .{ "UAA", null },
        .{ "UAG", null },
        .{ "UGA", null },
    });

    pub fn fromCodon(codon: []const u8) TranslationError!?Protein {
        return codon_table.get(codon) orelse TranslationError.InvalidCodon;
    }
};

pub fn proteins(allocator: mem.Allocator, strand: []const u8) (mem.Allocator.Error || TranslationError)![]Protein {
    var list: std.ArrayList(Protein) = .empty;
    errdefer list.deinit(allocator);

    var i: usize = 0;
    while (i < strand.len) : (i += 3) {
        const end: usize = @min(i + 3, strand.len);
        const protein = try Protein.fromCodon(strand[i..end]) orelse break;
        try list.append(allocator, protein);
    }

    return try list.toOwnedSlice(allocator);
}
