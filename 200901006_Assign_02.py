import re
import ast


def tokenization(expression):
    pattern = re.compile(r"[\w+\-()*^/]")
    return pattern.findall(expression)


def syntaxTree(expression):
    ST = ast.parse(expression)
    return ast.dump(ST, indent=4)


expression = input("Expression = ")
print(f"Tokens = {tokenization(expression)}")
print(f"Syntax Tree: \n{syntaxTree(expression)}")

