public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int low = 1, high = piles.Max();
        
        while (low <= high){
            int mid = low + (high-low) / 2;
            int time = 0;
            foreach (int pile in piles){
                time += (int)Math.Ceiling((double)pile / mid);
            }

            if (time <= h) high = mid-1;
            else low = mid+1;
        }

        return low;
    }
}
