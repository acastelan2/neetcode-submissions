/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    int getHeight(TreeNode* root, bool& isBalanced){
        if (!root) return 0;
        int left = getHeight(root->left, isBalanced);
        int right = getHeight(root->right, isBalanced);

        if (isBalanced){
            isBalanced = abs(left-right) <= 1;
        } 
        return 1 + max(left, right);
    }
public:
    bool isBalanced(TreeNode* root) {
        bool isBalanced = true;
        getHeight(root, isBalanced);
        return isBalanced;
    }
};
