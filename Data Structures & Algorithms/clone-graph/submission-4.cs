/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    private Node DFS(Node node, Dictionary<Node, Node> clones){
        if (node == null) return null;

        if (clones.TryGetValue(node, out var clone)){
            return clone;
        }

        var copy = new Node(node.val);
        clones[node] = copy;

        foreach (var nei in node.neighbors){
            copy.neighbors.Add(DFS(nei, clones));
        }

        return copy;
    }
    public Node CloneGraph(Node node) {
        var dict = new Dictionary<Node, Node>();
        return DFS(node, dict);
    }
}
