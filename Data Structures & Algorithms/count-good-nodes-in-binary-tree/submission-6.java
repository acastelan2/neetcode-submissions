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

        int count = 0;
        if (node.val >= ancestorMax){
            count = 1;
            ancestorMax = node.val;
        }

        count += preOrder(node.left, ancestorMax);
        count += preOrder(node.right, ancestorMax);

        return count;
    }
    public int goodNodes(TreeNode root) {
        return preOrder(root, Integer.MIN_VALUE);
    }
}
