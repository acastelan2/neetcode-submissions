/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode();
        ListNode* dummy = res;
        int carry = 0;
       
        while (l1 != nullptr || l2 != nullptr || carry != 0){
            int val1 = l1 != nullptr ? l1->val : 0;
            int val2 = l2 != nullptr ? l2->val : 0;
            int sum = val1 + val2 + carry;

            if (sum > 9){
                sum -= 10;
                carry = 1;
            }
            else{
                carry = 0;
            }

            dummy->next = new ListNode(sum);
            dummy = dummy->next;

            if (l1 != nullptr){
                l1 = l1->next;
            }
            if (l2 != nullptr){
                l2 = l2->next;
            }            
        }

        return res->next;
    }
};
