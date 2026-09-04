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
    void dfs(TreeNode* node, int k, vector<int>& vec){
        if (!node) return;

        dfs(node->left, k, vec);

        if (vec.size() < k){
            vec.push_back(node->val);
        }
        else return;

        dfs(node->right, k , vec);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> res;
        dfs(root, k, res);
        return res.back();
    }
};
