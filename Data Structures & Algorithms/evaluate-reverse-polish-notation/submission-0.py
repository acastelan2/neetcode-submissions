class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()
                val = ops[t](stack[-1], b)
                stack[-1] = val

        return stack[-1]