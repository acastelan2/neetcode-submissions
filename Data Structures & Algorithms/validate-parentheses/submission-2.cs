public class Solution {
    public bool IsValid(string s) {
        var stk = new Stack<char>();

        foreach (char c in s){
            if (c == '[') stk.Push(']');
            else if (c == '(') stk.Push(')');
            else if (c == '{') stk.Push('}');
            else{
                if (stk.Count != 0 && stk.Peek() == c) stk.Pop();
                else return false;
            }
        }

        return stk.Count == 0;

    }
}
