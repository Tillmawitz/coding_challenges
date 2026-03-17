"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:

Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:

    The number of nodes in the list is in the range [1, 105].
    1 <= Node.val <= 105
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Beat 90% on memory, but only 8% on speed. Uses constant memory and linear time complexity so not a bad solution by any means, but clearly a "faster" approach.
class initalSolution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 1
        working_node = head

        while working_node.next != None:
            counter += 1
            working_node = working_node.next
        
        if counter == 1:
            return None
        else:
            middle = counter // 2
            # Reset variables for reuse
            counter = 1
            working_node = head
            
            while counter < middle:
                counter += 1
                working_node = working_node.next

            working_node.next = working_node.next.next

        return head

# By using a fast pointer that always jumps 2 and a slow pointer that only jumps 1, we can iterate through the list only once. When the fast and fast.next (to account for even or odd lengths) condition is broken, slow will always be at the node before the middle. This solution is still constant memory, but beats 41% of solutions in speed. Side note, simpler lookup and earlier return for the edge case of list length 1.
class slightlyBetterSolution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return head