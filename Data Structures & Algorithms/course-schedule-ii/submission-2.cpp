class Solution {
private:
    static constexpr int visiting = 1;
    static constexpr int explored = 2;

    bool dfs(int course, const vector<vector<int>>& adjList, vector<int>& visited, vector<int>& res){
        if (visited[course] == visiting) return false;
        if (visited[course] == explored) return true; 

        visited[course] = visiting;
        for (int prq : adjList[course]){
            if (!dfs(prq, adjList, visited, res)) return false;
        }

        visited[course] = explored;
        res.push_back(course);
        return true;
    }
public:
    vector<int> findOrder(int numCourses, const vector<vector<int>>& prerequisites) {
        vector<int> res;
        vector<vector<int>> adjList(numCourses);
        vector<int> visited(numCourses, 0);

        for (const auto& p : prerequisites){
            adjList[p[0]].push_back(p[1]);
        }

        for (int i = 0; i < numCourses; ++i){
            if (!dfs(i, adjList, visited, res)) return {};
        }

        return res;
    }
};
