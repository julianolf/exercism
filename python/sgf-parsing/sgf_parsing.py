from re import fullmatch, DOTALL
from enum import Enum

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


class SgfParser(object):
    State = Enum('State', 'START TREE KEY VALUE')
    validation_pattern = r'^\(;\(?;?([A-Z]{1,2}(\[.+\])+\)?)*\)$'

    def __init__(self, sgf_string):
        self.sgf_string = sgf_string.strip()
        self.sgf_tree = None
        self._decode()
    
    def _decode(self):
        if not fullmatch(self.validation_pattern, self.sgf_string, DOTALL):
            raise ValueError('Invalid SGF string')
        
        nodes = []
        cur_state = self.State.START
        escape = False

        for char in self.sgf_string:
            if cur_state == self.State.START and char == '(':
                cur_state = self.State.TREE
            elif cur_state == self.State.TREE and char == ';':
                nodes.append(SgfTree())
                cur_state = self.State.KEY
                key = ''
            elif cur_state == self.State.KEY:
                if char == ')' and key and values:
                    nodes[-1].properties[key] = values
                elif char == '(':
                    nodes[-1].properties[key] = values
                    if len(nodes) > 2:
                        node = nodes.pop()
                        nodes[-1].children.append(node)
                elif char == ';':
                    nodes[-1].properties[key] = values
                    if len(nodes) > 1:
                        node = nodes.pop()
                        nodes[-1].children.append(node)
                    nodes.append(SgfTree())
                    key = ''
                elif char == '[':
                    value = ''
                    if key not in nodes[-1].properties:
                        nodes[-1].properties[key] = []
                        values = nodes[-1].properties[key]
                    cur_state = self.State.VALUE
                else:
                    key += char
            elif cur_state == self.State.VALUE:
                if char == '\\':
                    escape = True
                elif not escape and value and char == ']':
                    values.append(value)
                    value = ''
                    cur_state = self.State.KEY
                elif char == '\t':
                    value += ' '
                else:
                    value += char
                    escape = False
            else:
                raise ValueError('Parse error')
        
        while len(nodes) > 1:
            node = nodes.pop()
            nodes[-1].children.append(node)

        self.sgf_tree = nodes.pop()
    
    @staticmethod
    def parse(input_string=''):
        sgf_parser = SgfParser(input_string)
        return sgf_parser.sgf_tree

def parse(input_string=''):
    return SgfParser.parse(input_string)
