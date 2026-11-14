class Solution {
private:
    int memo(int i, span<const int> houses, vector<int>& cache){
        if (i >= houses.size()) return 0;
        if (cache[i] != -1) return cache[i];

        cache[i] = houses[i] + max
        (
            memo(i+2, houses, cache),
            memo(i+3, houses, cache)
        );

        return cache[i];

    }

    int slice(span<const int> houses){
        vector<int> cache(houses.size(), -1);
        return max(memo(0, houses, cache), memo(1, houses, cache));
    }

public:
    int rob(const vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        return max
        (  
            slice(span(nums).first(nums.size()-1)),
            slice(span(nums).last(nums.size()-1))
        );
    }
};
