pub const ComputationError = error{IllegalArgument};

pub fn steps(number: usize) anyerror!usize {
    switch (number) {
        0 => return ComputationError.IllegalArgument,
        1 => return 0,
        2 => return 1,
        else => {
            var num: usize = number;
            var acc: usize = 0;

            while (num > 1) : (acc += 1) {
                if (num % 2 == 0) {
                    num /= 2;
                } else {
                    num = num * 3 + 1;
                }
            }

            return acc;
        },
    }
}
