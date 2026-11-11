public class Solution {
    private void DFS(int node, List<List<int>> adjList, bool[] visited){
        visited[node] = true;

        foreach (int neighbor in adjList[node]){
            if (!visited[neighbor]){
                DFS(neighbor, adjList, visited);
            }
        }
    }
    public int CountComponents(int n, int[][] edges) {
        var adjList = new List<List<int>>(n);
        var visited = new bool[n];        
        
        for (int i = 0; i < n; i++){
            adjList.Add(new List<int>());
        }

        foreach (var p in edges){
            adjList[p[0]].Add(p[1]);
            adjList[p[1]].Add(p[0]);
        }

        int res = 0;
        for (int node = 0; node < n; node++){
            if (!visited[node]){
                DFS(node, adjList, visited);
                res++;
            }
        }

        return res;           
    }
}
