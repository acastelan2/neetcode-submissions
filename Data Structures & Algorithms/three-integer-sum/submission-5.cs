public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        var res = new List<List<int>>();
        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++){            
            int num = nums[i];
            if (num > 0) break;
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int left = i+1, right = nums.Length-1;
            while (left < right){
                int sum = num + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else{
                    res.Add(new List<int>{num, nums[left], nums[right]});
                    left++;
                    right--;

                    while (nums[left] == nums[left-1] && left < right){
                        left++;
                    }
                }
            }
        }
        return res;
    }
}
