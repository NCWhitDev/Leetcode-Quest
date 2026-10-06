
#include <iostream>
#include <vector>
#include <algorithm> // Required for std::sort and std::find
#include <unordered_set>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr) return head;
    unordered_set<int> seen;                             // Create a set to store seen values
    seen.insert(head->val);                             // Insert the value of the head node into the set

    ListNode * prev = head;                            // Initialize a pointer to keep track of the previous node
    ListNode * curr = head->next;                   // Initialize a pointer to traverse the list starting from the second node  

    while(curr != nullptr)
    {
        if(seen.count(curr->val) > 0){              // If the current value is already in the set, it is a duplicate
            ListNode* temp = curr;                  // Store the current node in a temporary pointer
            prev->next = curr->next;                // Bypass the current node by linking the previous node to the next node
            curr = curr->next;                      // Move the current pointer to the next node
            delete temp;                            
        }
        else{
            seen.insert(curr->val);
            prev = curr;                            // Move the previous pointer to the current node
            curr = curr->next;                      // Move the current pointer to the next node
        }
    }
        return head;                                // Return the modified list with duplicates removed
    }
    // ===============================================================================================================

ListNode* buildList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < values.size(); i++) {
        curr->next = new ListNode(values[i]);
        curr = curr->next;
    }
    return head;
}

void printList(ListNode* head) {
    while (head != nullptr) {
        std::cout << head->val;
        if (head->next != nullptr) std::cout << " -> ";
        head = head->next;
    }
    std::cout << std::endl;
}


void TestCases() {
    std::vector<int> testCase1 = {1, 1, 2, 2, 3, 4, 4, 1};
    ListNode* head1 = buildList(testCase1);
    head1 = deleteDuplicates(head1);
    printList(head1);   // expect: 1 -> 2
}

int main()
{
    TestCases();
}
