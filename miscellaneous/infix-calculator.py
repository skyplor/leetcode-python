class Solution:
    def infix_calculator(self, arr: list[str]) -> int:
        '''
        We use 2 stacks, 1 for operand, 1 for operator
        Next, we read in the tokens and if the token is operand, push into operand stack.
        If token is operator, then we check against the operator at the top of the operator stack.
            - If the current operator is higher precedence than the prev one, or if current operator is == precedence as prev one but is right-associative, push it in.
            - else, we pop operand 2 times, and pop operator once, do the calculation, then push the result into operand stack and push the new token into operator stack
        '''
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        operand = []
        operator = []

        def compute(a: int, b: int, operation: str) -> int:
            if operation == '+':
                return a + b
            if operation == '-':
                return a - b
            if operation == '*':
                return a * b
            if operation == '/':
                return a // b
            if operation == '^':
                return a ** b
            return 0

        def is_operand(token: str) -> bool:
            if not token:
                return False
            start = 1 if token[0] == '-' else 0
            if len(token[start:]) == 0:
                return False
            for c in token[start:]:
                if not c.isdigit():
                    return False

            return True

        def is_right_associative(token: str) -> bool:
            return token == '^'

        for token in arr:
            if is_operand(token):
                operand.append(int(token))
            else:
                while operator and (precedence[token] < precedence[operator[-1]] or (precedence[token] == precedence[operator[-1]] and not is_right_associative(token))):
                    b = int(operand.pop())
                    a = int(operand.pop())
                    operation = operator.pop()
                    result = compute(a, b, operation)
                    operand.append(result)
                operator.append(token)

        while operator:
            b = int(operand.pop())
            a = int(operand.pop())
            operation = operator.pop()
            result = compute(a, b, operation)
            operand.append(result)

        return operand[0]


sol = Solution()
print(
    f'output: {sol.infix_calculator(["100", "+", "200", "/", "2", "*", "5", "+", "7"])}, expected: 607')
print(
    f'output: {sol.infix_calculator(["2", "^", "3", "^", "2"])}, expected: 512')
