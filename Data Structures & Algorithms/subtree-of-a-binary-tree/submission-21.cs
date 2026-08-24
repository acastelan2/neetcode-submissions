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

    private bool IsSameRoot(TreeNode root, TreeNode subRoot){
        if (root == null && subRoot == null) return true;

        if (root != null && subRoot != null && root.val == subRoot.val){
            return IsSameRoot(root.left, subRoot.left) && IsSameRoot(root.right, subRoot.right);
        }

        return false;
    } 

    private bool IsDiffRoot(TreeNode root, TreeNode subRoot){
        if (subRoot == null) return true;
        if (root == null) return false;
        if (IsSameRoot(root, subRoot)) return true;

        return IsDiffRoot(root.left, subRoot) || IsDiffRoot(root.right, subRoot);  
    }

    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        return IsDiffRoot(root, subRoot);
    }
}
