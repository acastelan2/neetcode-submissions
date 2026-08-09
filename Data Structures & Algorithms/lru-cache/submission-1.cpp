class LRUCache {
private:
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    list<int> order;
    int capacity;

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()){
            return -1;
        }

        order.erase(it->second.second);
        order.push_back(key);
        it->second.second = prev(order.end());
        return it->second.first;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);

        if (it != cache.end()) {
            order.erase(it->second.second);
            order.push_back(key);
            it->second = {value, prev(order.end())};
        }
        else {
            if (cache.size() == capacity) {
                int lruKey = order.front();
                order.pop_front();
                cache.erase(lruKey);
            }

            order.push_back(key);
            cache.emplace(key, make_pair(value, prev(order.end())));
        }
    }
};
