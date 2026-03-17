"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Trickier than I thought, make sure to write out an example and go through it I originally forget to change what prev_node was pointing to.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head

        next_node = head.next.next if head.next.next else None
        working_node = head.next
        prev_node = head
        prev_node.next = None

        while working_node:
            working_node.next = prev_node
            prev_node = working_node
            working_node = next_node
            if next_node and next_node.next:
                next_node = next_node.next
            else:
                next_node = None

        return prev_node

# A cleaner written version, simplify man
class compactSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev