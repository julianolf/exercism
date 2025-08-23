class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class LinkedList:
    def __init__(self, values=None):
        self._head = None

        if values:
            self._head = Node(values[0])

            for value in values[1:]:
                node = Node(value)
                node.set_next(self._head)
                self._head = node

    def __iter__(self):
        node = self._head

        while node is not None:
            yield node.value()
            node = node.next()

    def __len__(self):
        return sum(1 for _ in self)

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        node = Node(value)

        if self._head is None:
            self._head = node
        else:
            node.set_next(self._head)
            self._head = node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        node = self._head
        self._head = self._head.next()

        return node.value()

    def reversed(self):
        return reversed([value for value in self])


class EmptyListException(Exception):
    pass
