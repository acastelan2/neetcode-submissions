public class Solution {
    private const int Visiting = 1;
    private const int Explored = 2;

    private bool DFS(int crs, List<List<int>> adjList, int[] visited){
        if (visited[crs] == Visiting) return false;
        if (visited[crs] == Explored) return true;

        visited[crs] = Visiting;
        foreach (var prereq in adjList[crs]){
            if (!DFS(prereq, adjList, visited)) return false;
        }

        visited[crs] = Explored;
        return true;
    }
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var adjList = new List<List<int>>(numCourses);
        var visited = new int[numCourses];

        for (int i = 0; i < numCourses; i++){
            adjList.Add(new List<int>());
        }

        foreach (var p in prerequisites){
            adjList[p[0]].Add(p[1]);
        }

        for (int course = 0; course < numCourses; course++){
            if (!DFS(course, adjList, visited)) return false;
        }

        return true;
    }
}
