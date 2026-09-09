class Solution {
private:
    priority_queue<int> maxHeap;
    
    int getHeaviestStone(){
        int stone = maxHeap.top();
        maxHeap.pop();
        return stone;
    }
    
public:
    int lastStoneWeight(vector<int>& stones) {
        for (int stone : stones){
            maxHeap.push(stone);
        }

        while (maxHeap.size() > 1){
            const int stone1 = getHeaviestStone();
            const int stone2 = getHeaviestStone();

            if (stone1 == stone2) continue;
            
            maxHeap.push(abs(stone1-stone2));
            
        }

        return maxHeap.size() == 1 ? maxHeap.top() : 0;
    }
};
