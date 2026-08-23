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
    bool isSameRoot(TreeNode* root, TreeNode* subRoot){
        if (!root && !subRoot) return true;

        if (root && subRoot && root->val == subRoot->val){
            return isSameRoot(root->left, subRoot->left) && isSameRoot(root->right, subRoot->right);
        }

        return false;        
    }

    bool isDiffRoot(TreeNode* root, TreeNode* subRoot){
        if (!subRoot) return true;
        if (!root) return false;

        if (isSameRoot(root, subRoot)){
            return true;
        }
        
        return isDiffRoot(root->left, subRoot) || isDiffRoot(root->right, subRoot);
        
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return isDiffRoot(root, subRoot);
    }
};
