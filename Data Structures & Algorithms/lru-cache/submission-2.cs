public class LRUCache {
    private Dictionary<int, LinkedListNode<(int key, int value)>> cache;
    private LinkedList<(int key, int value)> order;
    private int capacity;

    public LRUCache(int capacity) {
        this.cache = new Dictionary<int, LinkedListNode<(int key, int value)>>();
        this.order = new LinkedList<(int key, int value)>();
        this.capacity = capacity;
    }
    
    public int Get(int key) {
        if (!cache.TryGetValue(key, out var node)){
            return -1;
        }

        order.Remove(node);
        order.AddLast(node);
        return node.Value.value;
    }
    
    public void Put(int key, int value) {
        if (cache.TryGetValue(key, out var node)){
            order.Remove(node);
            node.Value = (key, value);
            order.AddLast(node);
        }
        else{
            if (cache.Count == capacity){
                var lruKey = order.First.Value;
                order.RemoveFirst();
                cache.Remove(lruKey.key);
            }

            var newNode = new LinkedListNode<(int key, int value)>((key, value)); 
            order.AddLast(newNode);
            cache.Add(key, newNode);
        }
    }
}
