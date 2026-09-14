public class Solution {
    private int GetDistance(int[] point){
        return point[0]*point[0] + point[1]*point[1];
    }

    public int[][] KClosest(int[][] points, int k) {
        var res = new List<int[]>();
        var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));

        for (int i = 0; i < points.GetLength(0); i++){
            int distance = GetDistance(points[i]);

            if (maxHeap.Count < k){
                maxHeap.Enqueue(i, distance);
            }
            else if (maxHeap.TryPeek(out _, out int topDistance) && distance < topDistance){
                maxHeap.Dequeue();
                maxHeap.Enqueue(i, distance);
            }
        }

        while (maxHeap.Count > 0){
            res.Add(points[maxHeap.Dequeue()]);
        }

        return res.ToArray();
    }
}
