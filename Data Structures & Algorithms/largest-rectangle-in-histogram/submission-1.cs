public class Solution {
    public int LargestRectangleArea(int[] heights) {
        int res = 0;
        int n = heights.Length;
        var stk = new Stack<int>();

        for (int i = 0; i <= n; i++){
            while (stk.Count != 0 && (i == n || heights[i] < heights[stk.Peek()])){
                int height = heights[stk.Peek()];
                stk.Pop();

                int left = stk.Count == 0 ? -1 : stk.Peek();
                int width = i-left-1;

                res = Math.Max(res, height*width);
            }

            stk.Push(i);
        }

        return res;
        
    }
}
