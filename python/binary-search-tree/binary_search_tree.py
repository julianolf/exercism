class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return (
            f"TreeNode(data={self.data}, "
            f"left={self.left}, "
            f"right={self.right})"
        )


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = None

        for data in tree_data:
            node = TreeNode(data)

            if self.tree is None:
                self.tree = node
            else:
                self.add_node(node)

    def add_node(self, node):
        current_node = self.tree

        while True:
            if node.data <= current_node.data:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    break

        if node.data <= current_node.data:
            current_node.left = node
        else:
            current_node.right = node

    def sorted(self, tree):
        if tree.left is None and tree.right is None:
            return [tree.data]

        if tree.left is not None and tree.right is None:
            return self.sorted(tree.left) + [tree.data]

        if tree.left is None and tree.right is not None:
            return [tree.data] + self.sorted(tree.right)

        return self.sorted(tree.left) + [tree.data] + self.sorted(tree.right)

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.sorted(self.tree) if self.tree is not None else []
