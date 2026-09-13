public class Solution {  

    public int LastStoneWeight(int[] stones) {
        PriorityQueue<int, int> maxHeap = new(Comparer<int>.Create((a, b) => b.CompareTo(a)));

        foreach (int stone in stones){
            maxHeap.Enqueue(stone,stone);
        }

        while (maxHeap.Count > 1){
            int stone1 = maxHeap.Dequeue();
            int stone2 = maxHeap.Dequeue();

            if (stone1 == stone2) continue;

            int newStone = Math.Abs(stone1-stone2);
            maxHeap.Enqueue(newStone,newStone);
        }

        return maxHeap.Count == 1 ? maxHeap.Peek() : 0;
    }
}
