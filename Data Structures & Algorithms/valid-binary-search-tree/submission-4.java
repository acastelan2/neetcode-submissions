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
    private boolean preOrder(TreeNode node, int low, int high){
        if (node == null) return true;
        if (low >= node.val || node.val >= high) return false;

        return preOrder(node.left, low, node.val) && preOrder(node.right, node.val, high);
    }
    public boolean isValidBST(TreeNode root) {
        return preOrder(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
}
