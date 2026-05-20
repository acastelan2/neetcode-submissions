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
    private int preorderIdx;
    private int[] preorder;
    private Map<Integer, Integer> inorderMap;

    private TreeNode build(int left, int right){
        if (left > right) return null;

        TreeNode node = new TreeNode();
        node.val = preorder[preorderIdx];
        preorderIdx++;

        int inorderIdx = inorderMap.get(node.val);
        node.left = build(left, inorderIdx-1);
        node.right = build(inorderIdx+1, right);
        return node;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        preorderIdx = 0;
        inorderMap = new HashMap<>();
        
        for (int i = 0; i < inorder.length; ++i){
            inorderMap.put(inorder[i], i);
        }
        return build(0, preorder.length-1);
    }
}
