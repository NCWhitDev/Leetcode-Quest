def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # dummy Node
        cur = dummy # Cursor points to dummy Node

        while list1 and list2: # While both lists are not empty | O(n)
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next

        cur.next = list1 if list1 else list2

        return dummy.next
