class Solution {
private:
    static constexpr int visiting = 1;
    static constexpr int explored = 2;

    bool dfs(int crs, vector<vector<int>>& adjList, vector<int>& visited){
        if (visited[crs] == visiting) return false;
        if (visited[crs] == explored) return true;

        visited[crs] = visiting;
        for (int prq : adjList[crs]){
            if (!dfs(prq, adjList, visited)) return false;
        }

        visited[crs] = explored;
        return true;
    }
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses);
        vector<int> visited(numCourses, 0);

        for (const auto& p : prerequisites){
            adjList[p[0]].push_back(p[1]);
        }

        for (int i = 0; i < numCourses; ++i){
            if (!dfs(i, adjList, visited)) return false;
        }

        return true;
    }
};
