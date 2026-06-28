public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var stk = new Stack<double>();

        var cars = position.Zip(speed, (pos,spd) => (pos,spd)).ToList();
        cars.Sort((a,b) => b.pos.CompareTo(a.pos));

        double leadingTime = 0;
        foreach (var (pos,spd) in cars){
            stk.Push((double)(target-pos)/spd);

            if (stk.Count > 1 && stk.Peek() <= leadingTime) stk.Pop();

            leadingTime = stk.Peek();
        }

        return stk.Count;
    }
}
