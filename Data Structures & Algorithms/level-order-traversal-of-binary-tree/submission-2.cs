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
    private void DFS(TreeNode root, List<List<int>> list, int level){
        if (root == null) return;
        if (level >= list.Count){
            list.Add(new List<int>());
        }

        list[level].Add(root.val);
        DFS(root.left, list, level+1);
        DFS(root.right, list, level+1);
    }

    public List<List<int>> LevelOrder(TreeNode root) {
        var res = new List<List<int>>();
        DFS(root, res, 0);
        return res;
    }
}
