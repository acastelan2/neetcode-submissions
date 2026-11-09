class Solution {
private:
    bool dfs(int nodeA, int nodeB, const vector<vector<int>>& adjList, vector<bool>& visited){
        if (nodeB == nodeA) return true;

        visited[nodeB] = true;

        for (int neighbor : adjList[nodeB]){
            if (!visited[neighbor]){
                if (dfs(nodeA, neighbor, adjList, visited)){
                    return true;
                }
            }
        }  

        return false;
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<vector<int>> adjList(edges.size()+1);
        vector<int> res(2);

        for (const auto& e : edges){
            vector<bool> visited(edges.size()+1);

            adjList[e[0]].push_back(e[1]);            
            if (dfs(e[0], e[1], adjList, visited)){
                return {e[0], e[1]};
            }
            
            adjList[e[1]].push_back(e[0]);
        }

        return res;
    }
};
