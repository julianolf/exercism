pub fn LinkedList(comptime T: type) type {
    return struct {
        const Self = @This();

        pub const Node = struct {
            prev: ?*Node = null,
            next: ?*Node = null,
            data: T,
        };

        first: ?*Node = null,
        last: ?*Node = null,
        len: usize = 0,

        pub fn push(self: *Self, node: *Node) void {
            node.prev = self.last;
            node.next = null;

            if (self.last) |last| last.next = node else self.first = node;

            self.last = node;
            self.len += 1;
        }

        pub fn pop(self: *Self) ?*Node {
            const node = self.last orelse return null;
            self.unlink(node);
            return node;
        }

        pub fn shift(self: *Self) ?*Node {
            const node = self.first orelse return null;
            self.unlink(node);
            return node;
        }

        pub fn unshift(self: *Self, node: *Node) void {
            node.prev = null;
            node.next = self.first;

            if (self.first) |first| first.prev = node else self.last = node;

            self.first = node;
            self.len += 1;
        }

        pub fn delete(self: *Self, node: *Node) void {
            var curr = self.first;
            while (curr) |n| : (curr = n.next) {
                if (n == node) return self.unlink(node);
            }
        }

        fn unlink(self: *Self, node: *Node) void {
            if (node.prev) |prev| prev.next = node.next else self.first = node.next;
            if (node.next) |next| next.prev = node.prev else self.last = node.prev;
            node.prev = null;
            node.next = null;
            self.len -= 1;
        }
    };
}
