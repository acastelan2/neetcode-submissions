public class Solution {
    public int LongestConsecutive(int[] nums) {
        var hSet = new HashSet<int>(nums);
        int res = 0;

        foreach (int num in hSet){
            if (!hSet.Contains(num-1)){
                int currNum = num;
                int length = 1;

                while (hSet.Contains(currNum+1)){
                    currNum++;
                    length++;
                }

                res = Math.Max(res, length);
            }
        }

        return res;
    }
}
