class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None: #add a '.' along the characters
        current = self.root
        for c in word:
            i = ord(c) - ord('a')
            if current.children[i] is None:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.isWord = True

    def search(self, word: str) -> bool:
        def subSearch(current, word, pos):
            if len(word) == pos:
                return current.isWord

            char = word[pos]
            if char != '.':
                i = ord(char) - ord('a')
                if current.children[i] is None:
                    return False
                return subSearch(current.children[i], word, pos+1)
            else:
                for i in range(0,25):
                    if current.children[i] is not None:
                        if subSearch(current.children[i], word, pos+1):
                            return True
           
            return False
        
        return subSearch(self.root, word, 0)  
        
