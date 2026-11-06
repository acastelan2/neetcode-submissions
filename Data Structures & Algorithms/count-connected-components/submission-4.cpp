class Solution {
private:
    void dfs(int node, const vector<vector<int>>& adjList, vector<bool>& visited){
        visited[node] = true;

        for (int neighbor : adjList[node]){
            if (!visited[neighbor]){
                dfs(neighbor, adjList, visited);
            }
        }        
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);
        vector<bool> visited(n, false);

        for (const auto& e : edges){
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }

        int res = 0;
        for (int node = 0; node < n; ++node){
            if (!visited[node]){
                dfs(node, adjList, visited);
                res++;
            }
        }

        return res;
    }
};
