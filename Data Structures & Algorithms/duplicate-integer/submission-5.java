class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int num: nums){
            hs.add(num);
        }
        return nums.length != hs.size();
    }
}