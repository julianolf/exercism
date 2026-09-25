pub fn squareRoot(radicand: usize) usize {
    if (radicand == 0)
        return 0;
    if (radicand <= 3)
        return 1;

    var sqrt: usize = 0;
    var op: usize = radicand;

    var one: usize = 1;
    while (one <= op) {
        one <<= 2;
    }
    one >>= 2;

    while (one != 0) {
        if (op >= sqrt + one) {
            op -= sqrt + one;
            sqrt += 2 * one;
        }
        sqrt /= 2;
        one /= 4;
    }

    return sqrt;
}
