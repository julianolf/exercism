class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None for _ in range(capacity)]
        self.new = 0
        self.old = 0

    def read(self):
        value = self.buffer[self.old]

        if value is None:
            raise BufferEmptyException("Circular buffer is empty")

        self.buffer[self.old] = None
        self.old = (self.old + 1) % len(self.buffer)

        return value

    def write(self, data):
        if self.buffer[self.new] is not None:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.new] = data
        self.new = (self.new + 1) % len(self.buffer)

    def overwrite(self, data):
        self.buffer[self.new] = None

        if self.new == self.old:
            self.old = (self.old + 1) % len(self.buffer)

        self.write(data)

    def clear(self):
        self.old = self.new

        for i in range(len(self.buffer)):
            self.buffer[i] = None
