public class Solution {
    public string MinWindow(string s, string t) {
        const int MAXLENGTH = 1000;
        var count = new Dictionary<char,int>();
        var window = new Dictionary<char,int>();

        foreach (char c in t){
            count[c] = count.GetValueOrDefault(c, 0) + 1;
        }

        int uniqueChars = count.Count;
        int currLen = 0, left = 0, start = 0;
        int end = MAXLENGTH;

        for (int right = 0; right < s.Length; right++){
            char rc = s[right];

            int rcVal = window.GetValueOrDefault(rc, 0) + 1;
            window[rc] = rcVal;
            
            if (count.TryGetValue(rc, out int ctVal)){
                if (ctVal == rcVal){
                    currLen++;
                } 
            }

            while (currLen == uniqueChars){
                if (right-left+1 < end){
                    end = right-left+1;
                    start = left;
                }

                char lc = s[left];

                int lcVal = window.GetValueOrDefault(lc, 0) - 1;
                window[lc] = lcVal;

                if (count.TryGetValue(lc, out int val)){
                    if (val > lcVal) {
                        currLen--;
                    }
                }

                left++;
            }
        }

        return end == MAXLENGTH ? "" : s.Substring(start, end);
    }
}
