# Definition for singly-linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        currentA, currentB = A, B
        if A == None:
            return B
        elif B == None:
            return A
        if currentA.val <= currentB.val:
            C = currentA
            currentA = currentA.next
        else:
            C = currentB
            currentB = currentB.next
        currentC = C
        while currentA is not None and currentB is not None:
            if currentA.val <= currentB.val:
                currentC.next = currentA
                currentA = currentA.next
                currentC = currentC.next
            else:
                currentC.next = currentB
                currentB = currentB.next
                currentC = currentC.next

        while currentA is not None:
            currentC.next = currentA
            currentA = currentA.next
            currentC = currentC.next

        while currentB is not None:
            currentC.next = currentB
            currentB = currentB.next
            currentC = currentC.next
        return C


l1 = ListNode(1)
l1.next = ListNode(2)
# l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = Solution().mergeTwoLists(l1, l2)

print()

while result:
    print(result.val)
    result = result.next
