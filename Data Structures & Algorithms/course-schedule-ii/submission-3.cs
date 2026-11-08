public class Solution {
    private const int Visiting = 1;
    private const int Explored = 2;

    private bool DFS(int course, List<List<int>> adjList, int[] visited, List<int> res){
        if (visited[course] == Visiting) return false;
        if (visited[course] == Explored) return true; 

        visited[course] = Visiting;
        foreach (int prq in adjList[course]){
            if (!DFS(prq, adjList, visited, res)) return false;
        }

        visited[course] = Explored;
        res.Add(course);
        return true;
    }
    public int[] FindOrder(int numCourses, int[][] prerequisites) {
        var res = new List<int>();
        var adjList = new List<List<int>>();
        var visited = new int[numCourses];

        for (int i = 0; i < numCourses; i++){
            adjList.Add(new List<int>());
        }

        foreach (var p in prerequisites){
            adjList[p[0]].Add(p[1]);
        }

        for (int course = 0; course < numCourses; course++){
            if (!DFS(course, adjList, visited, res)) return [];
        }

        return res.ToArray();
    }
}
