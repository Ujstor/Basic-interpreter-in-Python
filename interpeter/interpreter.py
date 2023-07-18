from tokens import Integer, Float


class Interpreter:
    def __init__ (self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def read_VAR(self, id):
        variable = self.data.read(id)
        variable_type = variable.type

        return getattr(self, f'read_{variable_type}')(variable.value)

    #1) make a = 5
    #2) make b = a + 1
    #[b, =, [a, +, 1]]

    def compute_bin(self, left, op, right):
        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)

        if op.value == '=':
            #1) make a = 5
            left_type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

        left =  getattr(self, f'read_{left_type}')(left.value)
        right = getattr(self, f'read_{right_type}')(right.value)

        if op.value == '+':
            output =  left + right
        elif op.value == '-':
            output =  left - right
        elif op.value == '*':
            output = left * right
        elif op.value == '/':
            output = left / right

        return Integer(output) if (left_type == 'INT' and right_type == 'INT') else Float(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree
        #   A
        #  / \
        # B   C
        #[1, +, 1]
        #[[1, +, 2], +, 3]] ---> 1 + 2 + 3
        left_node = tree[0] # evaluate left subtree
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2] # evaluate right subtree
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1] # Root node

        return self.compute_bin(left_node, operator, right_node)