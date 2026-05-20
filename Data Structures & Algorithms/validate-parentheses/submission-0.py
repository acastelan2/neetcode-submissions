class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        return len(stack) == 0