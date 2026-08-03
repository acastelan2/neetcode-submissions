/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> uMap;

        Node* curr = head;
        while (curr != nullptr){
            uMap[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;
        while (curr != nullptr){
            Node* copy = uMap[curr];
            copy->next = uMap[curr->next];
            copy->random = uMap[curr->random];
            curr = curr->next;
        }

        return uMap[head];
    }
};
