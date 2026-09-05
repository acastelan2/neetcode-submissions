/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    private void DFS(TreeNode node, int k, List<int> list){
        if (node == null) return;

        DFS(node.left, k, list);

        if (list.Count < k){
            list.Add(node.val);
        }
        else return;

        DFS(node.right, k, list);
    }
    public int KthSmallest(TreeNode root, int k) {
        var res = new List<int>();
        DFS(root, k, res);
        return res[^1];
    }
}
