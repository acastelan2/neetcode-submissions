public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var res = new int[temperatures.Length];
        var temps = new Stack<int>();
        var idx = new Stack<int>();

        temps.Push(temperatures[0]);
        idx.Push(0);

        for (int i = 0; i < temperatures.Length; i++){
            while (temps.Count > 0 && temperatures[i] > temps.Peek()){
                res[idx.Peek()] = i - idx.Peek();
                temps.Pop();
                idx.Pop();
            }

            temps.Push(temperatures[i]);
            idx.Push(i);
        }

        return res;
    }
}
