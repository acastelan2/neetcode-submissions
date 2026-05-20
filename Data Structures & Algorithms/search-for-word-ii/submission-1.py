class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
        self.index = -1

class Solution:
    def __init__(self):
        self.root = TrieNode()
        

    def _addWord(self, idx: int, word: str) -> bool:
        current = self.root
        for c in word:
            i = ord(c) - ord('a')
            if current.children[i] is None:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.isWord = True
        current.index = idx

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row, col, node, res):
            char = board[row][col]
            i = ord(char) - ord('a')
            current = node
            if current.children[i] is None:
                return

            current = current.children[i]
            if current.isWord and current.index != -1:
                res.append(words[current.index])
                current.index = -1
            
            board[row][col] = " "
            for nr,nc in neighbors:
                r,c = nr+row, nc+col
                if 0 <= r < m and 0 <= c < n and board[r][c] != " ":
                    dfs(r, c, current, res)

            board[row][col] = char
        
        for i,word in enumerate(words):
            self._addWord(i,word)

        m = len(board)
        n = len(board[0])
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = []
        for row in range(m):
            for col in range(n):
               dfs(row, col, self.root, res)

        return res
