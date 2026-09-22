pub fn eggCount(number: usize) usize {
    var n: usize = number;
    var c: usize = 0;

    while (n != 0) : (c += 1) {
        n &= n - 1;
    }

    return c;
}
