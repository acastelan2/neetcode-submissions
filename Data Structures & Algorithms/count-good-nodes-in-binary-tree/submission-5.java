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
    private int maxVal;
    private int count;

    public Solution(){
        this.maxVal = Integer.MIN_VALUE;
        this.count = 0;
    }
    private void preOrder(TreeNode node){
        if (node == null) return;
        int ancestorVal = node.val;
        if (node.val >= this.maxVal){
            this.maxVal = node.val;
            this.count++;
        }
        else ancestorVal = this.maxVal;

        preOrder(node.left);
        this.maxVal = ancestorVal;
        preOrder(node.right);
    }
    public int goodNodes(TreeNode root) {
        preOrder(root);
        return this.count;
    }
}
