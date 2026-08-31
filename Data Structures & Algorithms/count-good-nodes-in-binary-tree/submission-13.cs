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
    private int DFS(TreeNode root, int maxVal){
        if (root == null) return 0;
        
        int count = 0;
        if (root.val >= maxVal){
            count = 1;
            maxVal = root.val;
        }

        count += DFS(root.left, maxVal);
        count += DFS(root.right, maxVal);

        return count;
    }
    public int GoodNodes(TreeNode root) {
        return DFS(root, int.MinValue);
    }
}
