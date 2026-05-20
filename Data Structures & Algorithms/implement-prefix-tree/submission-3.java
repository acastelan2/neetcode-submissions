class TreeNode{
    private TreeNode[] children;
    private boolean isWord;
    public TreeNode(){
        children = new TreeNode[26];
    }
}

class PrefixTree {
    private TreeNode root;
    public PrefixTree() {
        root = new TreeNode();
    }

    public void insert(String word) {
        TreeNode current = root;
        for (char c: word.toCharArray()){
            int i = c - 'a';            
            if (current.children[i] == null){
                current.children[i] = new TreeNode();
            }
            current = current.children[i];
        }
        current.isWord = true;
    }

    public boolean search(String word) {
        TreeNode current = root;
        for (char c: word.toCharArray()){
            int i = c - 'a';
            if (current.children[i] == null){
                return false;
            }
            current = current.children[i];
        }
        return current.isWord;
    }

    public boolean startsWith(String prefix) {
        TreeNode current = root;
        for (char c: prefix.toCharArray()){
            int i = c - 'a';
            if (current.children[i] == null){
                return false;
            }
            current = current.children[i];
        }
        return true;
    }
}
