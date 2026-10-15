/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    Node* dfs(Node* node, unordered_map<Node*, Node*>& uMap){
        if (!node) return nullptr;
        
        auto it = uMap.find(node);
        if (it != uMap.end()) return it->second;

        auto* copy = new Node(node->val);
        uMap[node] = copy;

        for (auto* nei: node->neighbors){
            copy->neighbors.push_back(dfs(nei, uMap));
        }

        return copy;

    }
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> uMap;
        return dfs(node, uMap);        
    }
};
