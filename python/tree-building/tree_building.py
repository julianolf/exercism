class Record(object):
    def __init__(self, record_id = 0, parent_id = 0):
        self.record_id = record_id
        self.parent_id = parent_id


class Node(object):
    def __init__(self, node_id = 0):
        self.node_id = node_id
        self.children = []
    
    def add_child(self, node):
        if not node or not isinstance(node, Node):
            raise ValueError('Parameter `node` must be of type Node.')
        if self.node_id > node.node_id:
            raise ValueError('Parent id must be lower than child id.')
        self.children.append(node)


class Tree(object):
    def __init__(self):
        self._root = None
        self._next_idx = 0

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, record):
        if not record or not isinstance(record, Record):
            raise ValueError('Parameter `record` must be of type Record.')
        if record.record_id != 0:
            raise ValueError('Root tree must start with id 0.')
        if record.parent_id != 0:
            raise ValueError('Root node cannot have a parent.')
        self._root = Node(record.record_id)
        self._next_idx = 1
    
    def _find_branch(self, parent_id):
        if self._root.node_id == parent_id:
            return self._root
        else:
            def search(nodes, node_id):
                for node in nodes:
                    if type(node) == list:
                        search(node, node_id)
                    elif node.node_id == node_id:
                        return node
                raise ValueError('Parent node not found.')
            return search(self._root.children, parent_id)
    
    def grow(self, record):
        if not record or not isinstance(record, Record):
            raise ValueError('Parameter `record` must be of type Record.')
        if record.record_id == record.parent_id != 0:
            raise ValueError('Tree is a cycle.')
        if not self._root:
            self.root = record
        else:
            if record.record_id != self._next_idx:
                raise ValueError('Tree must be continuous.')
            node = Node(record.record_id)
            parent = self._find_branch(record.parent_id)
            parent.add_child(node)
            self._next_idx += 1
    
    @staticmethod
    def build(records):
        tree = Tree()
        if isinstance(records, Record):
            tree.grow(records)
        elif type(records) == list and all(isinstance(s, Record) for s in records):
            records.sort(key=lambda r: r.record_id)
            for record in records:
                tree.grow(record)
        return tree


def build_tree(records):
    tree = Tree.build(records)
    return tree.root
