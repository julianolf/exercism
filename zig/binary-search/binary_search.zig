pub fn binarySearch(comptime T: type, target: T, items: []const T) ?usize {
    if (items.len == 0)
        return null;

    const middle: usize = items.len / 2;
    if (items[middle] == target)
        return middle;

    if (items[middle] > target)
        return binarySearch(T, target, items[0..middle]);

    if (binarySearch(T, target, items[middle + 1 ..])) |right|
        return middle + right + 1;

    return null;
}
