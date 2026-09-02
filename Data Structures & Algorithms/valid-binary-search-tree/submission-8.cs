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
    private bool DFS(TreeNode root, int minVal, int maxVal){
        if (root == null) return true;

        if (root.val <= minVal || root.val >= maxVal){
            return false;
        }

        return DFS(root.left, minVal, root.val) && DFS(root.right, root.val, maxVal);
    }
    public bool IsValidBST(TreeNode root) {
        return DFS(root, int.MinValue, int.MaxValue);
    }
}
