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
    private int GetHeight(TreeNode root, ref bool isBalanced){
        if (root == null) return 0;

        int left = GetHeight(root.left, ref isBalanced);
        int right = GetHeight(root.right, ref isBalanced);

        if (isBalanced){
            isBalanced = Math.Abs(left-right) <= 1;
        }

        return 1 + Math.Max(left, right);
    }

    public bool IsBalanced(TreeNode root) {
        bool isBalanced = true;
        GetHeight(root, ref isBalanced);
        return isBalanced;
    }
}
