/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    private int preOrder(TreeNode node, int ancestorMax){
        if (node == null) return 0;

        int res = (node.val >= ancestorMax) ? 1 : 0;
        ancestorMax = Math.max(ancestorMax, node.val);
        return res + preOrder(node.left, ancestorMax) + preOrder(node.right, ancestorMax);
    }
    public int goodNodes(TreeNode root) {
        return preOrder(root, root.val);
    }
}
