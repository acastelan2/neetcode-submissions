public class Solution {
    private bool DFS(int node, int initNode, List<List<int>> adjList, bool[] visited){
        if (visited[node]) return false;

        visited[node] = true;

        foreach (int edgeNode in adjList[node]){
            if (edgeNode == initNode) continue;
            
            if (!DFS(edgeNode, node, adjList, visited)){
                return false;
            }
        }

        return true;
    }
    public bool ValidTree(int n, int[][] edges) {
        if (edges.Length != n-1) return false;

        var adjList = new List<List<int>>(n);
        var visited = new bool[n];

        for (int i = 0; i < n; i++){
            adjList.Add(new List<int>());
        }

        foreach (var p in edges){
            adjList[p[0]].Add(p[1]);
            adjList[p[1]].Add(p[0]);
        }

        if (!DFS(0, -1, adjList, visited)) return false;

        foreach (bool v in visited){
            if (!v) return false;
        }

        return true;
    }
}
