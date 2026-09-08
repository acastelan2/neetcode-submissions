public class KthLargest {
    private PriorityQueue<int, int> minHeap = new();
    private readonly int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        foreach (int num in nums){
            AddToMinHeap(num);
        }
    }

    private void AddToMinHeap(int val){
        if (minHeap.Count < k){
            minHeap.Enqueue(val,val);
        }
        else if (val > minHeap.Peek()){
            minHeap.Dequeue();
            minHeap.Enqueue(val,val);
        }
    }
    
    public int Add(int val) {
        AddToMinHeap(val);
        return minHeap.Peek();
    }
}
