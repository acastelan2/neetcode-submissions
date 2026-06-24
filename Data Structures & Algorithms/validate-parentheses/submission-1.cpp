class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;

        for (char c : s){
            if (c == '[') stk.push(']');
            else if (c == '(') stk.push(')');
            else if (c == '{') stk.push('}');
            else{
                if (!stk.empty() && stk.top() == c) stk.pop();
                else return false;
            }
        }

        return stk.empty();
    }
};
