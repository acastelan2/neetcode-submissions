class PrefixTree {

    class Node {
        private final char letter;
        private final Node[] children;
        private boolean isWord;
        
        private Node(final char letter) {
            this.letter = letter;
            this.children = new Node[26];
        }
    }

    private final Node root;

    public PrefixTree() {
         root = new Node((char) 0);
    }

    public void insert(String word) {
        int index = 0;
        Node curr = root;

        while (index < word.length()) {
            final char letter = word.charAt(index);
            final int letterIndex = letter - 'a';
            Node temp = curr.children[letterIndex];
            if (temp == null) {
                temp = new Node(letter);
                curr.children[letterIndex] = temp;
            }
            curr = temp;
            index++;
        }
        curr.isWord = true;
    }

    public boolean search(String word) {
        int index = 0;
        Node curr = root;

        while (index < word.length()) {
            final char letter = word.charAt(index);
            final int letterIndex = letter - 'a';
            Node temp = curr.children[letterIndex];
            if (temp == null) {
                return false;
            }
            curr = temp;
            index++;
        }

        return curr.isWord;
    }

    public boolean startsWith(String prefix) {
        int index = 0;
        Node curr = root;

        while (index < prefix.length()) {
            final char letter = prefix.charAt(index);
            final int letterIndex = letter - 'a';
            Node temp = curr.children[letterIndex];
            if (temp == null) {
                return false;
            }
            curr = temp;
            index++;
        }

        return true;
    }
}
