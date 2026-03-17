"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:

    The number of nodes in the linked list is in the range [0, 104].
    -10^6 <= Node.val <= 10^6
"""

# Pretty simple, just get an even and odd pointer then iterate and set them to node.next.next. Edge cases are important for this one, and would be harder in a live interview. Need to remember to set even.next to None if even.next.next exists, otherwise we would create a cycle in the linked list as the last odd node would still be at the end of the even list.abs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # List length of 0 return None, 1 or 2 nothing needed
        if head == None:
            return None
        elif head.next == None or head.next.next == None:
            return head

        odd_working = head
        even_working = even_start = head.next

        # Need to make sure there is at least one more node before checking if there is a next odd node
        while odd_working.next and odd_working.next.next:
            odd_working.next = odd_working.next.next
            odd_working = odd_working.next

            if even_working.next.next:
                even_working.next = even_working.next.next
                even_working = even_working.next
            else:
                even_working.next = None

        odd_working.next = even_start

        return head