const std = @import("std");
const EnumSet = std.EnumSet;

pub const Allergen = enum {
    eggs,
    peanuts,
    shellfish,
    strawberries,
    tomatoes,
    chocolate,
    pollen,
    cats,
};

pub fn isAllergicTo(score: u8, allergen: Allergen) bool {
    const allergies = initAllergenSet(score);
    return allergies.contains(allergen);
}

pub fn initAllergenSet(score: usize) EnumSet(Allergen) {
    return .{ .bits = .{ .mask = @truncate(score) } };
}
