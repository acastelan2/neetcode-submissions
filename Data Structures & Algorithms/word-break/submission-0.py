class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True

            for j in wordLens:
                substr = s[i:i+j]
                if substr in wordSet and substr not in memo:
                    if dfs(i+j):
                        return True
                    memo.add(substr)
            
            return False
        
        wordSet = set(wordDict)
        wordLens = set([len(i) for i in wordDict])
        memo = set()
        return dfs(0)
