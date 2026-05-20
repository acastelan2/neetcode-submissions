class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(start):
            if start == len(s):
                res.append(sub.copy())
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    sub_string = s[start:end+1]
                    sub.append(sub_string)
                    backtrack(end+1)
                    sub.pop()


        sub, res = [], []
        backtrack(0)
        return res