from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.operate(token, num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]

    def operate(self, token, num1, num2):
        if token == '+':
            return num1 + num2
        elif token == '-':
            return num1 - num2
        elif token == '*':
            return num1 * num2
        elif token == '/':
            return int(num1 / num2)
