class Solution {
private: 
    int getDistance(const vector<int>& p) const{
        return p[0] * p[0] + p[1] * p[1];  //achieves the same purpose at lower computational cost
    }

public:
    vector<vector<int>> kClosest(const vector<vector<int>>& points, int k) {
        priority_queue<pair<int,int>> maxHeap;
        vector<vector<int>> res;

        for (size_t index = 0; const auto& point : points) {
            const int dist = getDistance(point);

            if (maxHeap.size() < k){                
                maxHeap.push({dist, index});
            }
            else if (dist < maxHeap.top().first){
                maxHeap.pop();
                maxHeap.push({dist, index});
            }

            index++; 
        }

        while (!maxHeap.empty()){
            res.push_back(points[maxHeap.top().second]);
            maxHeap.pop();
        }

        return res;
    }
};
