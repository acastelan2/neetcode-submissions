class Solution {
public:
    string minWindow(string s, string t) {
        const int MAXLENGTH = 1000;
        unordered_map<char,int> count;
        unordered_map<char,int> window;
        
        for (char c : t) count[c]++;

        int uniqueChars = count.size();
        int currLen = 0, left = 0, start = 0;
        int end = MAXLENGTH;

        for (int right = 0; right < s.size(); ++right){
            char rc = s[right];
            window[rc]++;

            auto itR = count.find(rc);
            if (itR != count.end() && itR->second == window[rc]) currLen++;
            
            while (currLen == uniqueChars){
                if (right-left+1 < end){
                    end = right-left+1;
                    start = left;
                }

                char lc = s[left];
                window[lc]--;

                auto itL = count.find(lc);
                if (itL != count.end() && itL->second > window[lc]) currLen--;

                left++;
            }           
        }

        return end == MAXLENGTH ? "" : s.substr(start,end);
    }
};
