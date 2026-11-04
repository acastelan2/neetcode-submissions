class Solution {
private:
    bool dfs(int node, int parent, const vector<vector<int>>& adjList, vector<bool>& visited){
        if (visited[node]) return false;

        visited[node] = true;

        for (int edgeNode : adjList[node]){
            if (edgeNode == parent) continue;
            
            if (!dfs(edgeNode, node, adjList, visited)){
                return false;
            }
        }

        return true;
    }
public:
    bool validTree(int n, const vector<vector<int>>& edges) {        
        if (edges.size() != n-1) return false;

        vector<vector<int>> adjList(n);
        vector<bool> visited(n, false);

        for (const auto& e : edges){
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }

        if (!dfs(0, -1, adjList, visited)) return false;

        for (bool v : visited){
            if (!v) return false;
        }

        return true;
    }
};
