class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for val in tokens:
            if val not in operators:
                stack.append(int(val))
            elif val in operators:
                a = stack.pop()
                b = stack.pop()
                if val == '+':
                    stack.append(a+b)
                if val == '-':
                    stack.append(b-a)
                if val == '*':
                    stack.append(a*b)
                if val == '/':
                    stack.append(int(b/a))

        return stack.pop()

        