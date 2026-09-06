class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    const int k;

    void addToMinHeap(int val){
        if (minHeap.size() < k){
            minHeap.push(val);
        }
        else if (val > minHeap.top()){
            minHeap.pop();
            minHeap.push(val);
        }
    }

public:
    KthLargest(int k, vector<int>& nums): k(k) {
        for (int num: nums){
            addToMinHeap(num);
        }
    }
    
    int add(int val) {
        addToMinHeap(val);
        return minHeap.top();
    }
};
