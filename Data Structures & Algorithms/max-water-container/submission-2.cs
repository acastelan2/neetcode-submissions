public class Solution {
    public int MaxArea(int[] heights) {
        int left = 0, right = heights.Length-1;
        int res = 0;

        while (left < right){
            int h = Math.Min(heights[left], heights[right]);
            int w = right-left;
            res = Math.Max(res, h*w);

            if (heights[left] < heights[right]) left++;
            else right--;
        }

        return res;
    }
}
