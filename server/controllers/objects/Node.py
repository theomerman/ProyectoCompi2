from controllers.operations.sum import sum
from controllers.operations.substract import substract
from controllers.operations.multiply import multiply
from controllers.operations.divide import divide
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def traverse(node : Node):
    if node is not None:
        left_value = traverse(node.left)
        right_value = traverse(node.right)
        # print(node.value, end=" ")
        # print(type(node.value))
        if left_value is None and right_value is None:
            return node.value
        if node.value in operators:
            return calculate(node.value, left_value, right_value)
    
    return None

operators = ['+', '-', '*', '/', '>', '<', '=', '>=', '<=', '!=', 'and', 'or', 'not', '&&', '||', '!']
def calculate(operation, left_value, right_value):
    # print(left_value," ", operation, " ", right_value)
    if operation == "+":
        result, err = sum(left_value, right_value)
        if err is not None:
            raise Exception(err)
        return result
    if operation == "-":
        return substract(left_value, right_value)
    if operation == "*":
        result, err = multiply(left_value, right_value)
        if err is not None:
            raise Exception(err)
        return result
    if operation == "/":
        result, err = divide(left_value, right_value)
        if err is not None:
            raise Exception(err)
        return result
    if operation == "=":
        return left_value == right_value
    if operation == '!=':
        return left_value != right_value
    if operation == '>':
        return left_value > right_value
    if operation == '<':
        return left_value < right_value
    if operation == '>=':
        return left_value >= right_value
    if operation == '<=':
        return left_value <= right_value
    if operation == '&&' or operation == 'and':
        return left_value and right_value
    if operation == '||' or operation == 'or':
        return left_value or right_value
    if operation == '!':
        return not left_value
    raise Exception("Operation not supported")
    

## create tree copy
def copy_tree(node:Node):
    if node is None:
        return None
    new_node = Node(node.value)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    return new_node

# def set_values(node:Node, values:list, column_names:list):
#     if node is not None:
#         set_values(node.left, values, column_names)
#         set_values(node.right, values, column_names)
#         # if node.value in column_names:
#         #     node.value = values[column_names.index(node.value)]
#         print(node.value)
#         return node
def set_values(node:Node, values:list, column_names:list):
    if node is not None:
        set_values(node.left, values, column_names)
        set_values(node.right, values, column_names)
        if node.value in column_names:
            node.value = values[column_names.index(node.value)]
        elif node.value in operators:
            pass
        else:
            raise Exception(f"Error: Column { node.value } not found")
        # print(node.value)
