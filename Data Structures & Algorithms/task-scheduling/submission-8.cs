public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        var counts = new int[26];
        int maxFreq = 0;
        int numMaxFreq = 0;

        foreach (char task in tasks){
            counts[task - 'A']++;
            maxFreq = Math.Max(maxFreq, counts[task- 'A']);
        }

        foreach (int count in counts){
            if (count == maxFreq){
                numMaxFreq++;
            }
        }

        int res = (maxFreq - 1) * (n+1) + numMaxFreq;
        return Math.Max(tasks.Length, res);
    }
}
