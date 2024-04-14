class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def perform_operation(x: int, y: int, operation: str):
            if operation == '+':
                return x + y
            elif operation == '-':
                return x - y
            elif operation == '*':
                return x * y
            elif operation == '/':
                return int(x / y)

        operations = set(('+', '-', '/', '*'))

        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                y = stack.pop()
                x = stack.pop()
                res = perform_operation(x, y, char)
                stack.append(res)
        return stack.pop()
