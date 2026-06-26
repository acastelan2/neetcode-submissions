public class Solution {
    public int EvalRPN(string[] tokens) {
        var stk = new Stack<int>();
        foreach (string t in tokens){
            if (t == "+" || t == "-" || t == "*" || t == "/"){
                int b = stk.Peek(); stk.Pop();
                int a = stk.Peek(); stk.Pop();

                if (t == "+") stk.Push(a+b);
                else if (t == "-") stk.Push(a-b);
                else if (t == "*") stk.Push(a*b);
                else stk.Push(a/b);
            }
            else stk.Push(int.Parse(t));
        }

        return stk.Peek();

    }
}
