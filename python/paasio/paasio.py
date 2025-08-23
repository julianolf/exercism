import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__read_bytes = 0
        self.__read_ops = 0
        self.__write_bytes = 0
        self.__write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        data = super().readline()

        if len(data) == 0:
            raise StopIteration

        self.__read_bytes += len(data)
        self.__read_ops += 1

        return data

    def read(self, size=-1):
        data = super().read(size)

        self.__read_bytes += len(data)
        self.__read_ops += 1

        return data

    @property
    def read_bytes(self):
        return self.__read_bytes

    @property
    def read_ops(self):
        return self.__read_ops

    def write(self, b):
        bytes_written = super().write(b)

        self.__write_bytes += bytes_written
        self.__write_ops += 1

        return bytes_written

    @property
    def write_bytes(self):
        return self.__write_bytes

    @property
    def write_ops(self):
        return self.__write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.__socket = socket
        self.__recv_bytes = 0
        self.__recv_ops = 0
        self.__send_bytes = 0
        self.__send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.__socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        data = self.__socket.recv(bufsize, flags)

        self.__recv_bytes += len(data)
        self.__recv_ops += 1

        return data

    @property
    def recv_bytes(self):
        return self.__recv_bytes

    @property
    def recv_ops(self):
        return self.__recv_ops

    def send(self, data, flags=0):
        bytes_sent = self.__socket.send(data, flags)

        self.__send_bytes += bytes_sent
        self.__send_ops += 1

        return bytes_sent

    @property
    def send_bytes(self):
        return self.__send_bytes

    @property
    def send_ops(self):
        return self.__send_ops
