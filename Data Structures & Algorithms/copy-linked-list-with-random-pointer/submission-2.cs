/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        Dictionary<Node, Node> dict = new Dictionary<Node, Node>();

        Node curr = head;
        while (curr != null) {
            dict[curr] = new Node(curr.val);
            curr = curr.next;
        }

        curr = head;
        while (curr != null) {
            Node copy = dict[curr];
            copy.next = curr.next == null ? null : dict[curr.next];
            copy.random = curr.random == null ? null : dict[curr.random];
            curr = curr.next;
        }

        return head == null ? null : dict[head];
    }
}