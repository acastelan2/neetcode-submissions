class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hm = new HashSet<Integer>();
        for (int num: nums){
            hm.add(num);
        }
        return nums.length != hm.size();
    }
}