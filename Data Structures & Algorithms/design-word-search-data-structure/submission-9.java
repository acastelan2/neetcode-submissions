class TrieNode{
    private TrieNode[] children;
    private boolean isWord;

    public TrieNode(){
        children = new TrieNode[26];
    }
}

class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode current = root;
        for (char c: word.toCharArray()){
            int i = c - 'a';
            if (current.children[i] == null){
                current.children[i] = new TrieNode();
            }
            current = current.children[i];
        }
        current.isWord = true;
    }

    public boolean search(String word) {
        return subSearch(root, word, 0);
    }

    private boolean subSearch(TrieNode current, String word, int pos){
        if (word.length() == pos) return current.isWord;

        char c = word.charAt(pos);
        if (c != '.'){
            int i = c - 'a';
            if (current.children[i] == null) return false;
            return subSearch(current.children[i], word, pos+1);
        }
        else{
            for (int i = 0; i < 26; ++i){
                if (current.children[i] != null){
                    if (subSearch(current.children[i], word, pos+1)) return true;
                }
            }
        }
        return false;
    }
}
