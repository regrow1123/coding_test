# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, prev):
            if not node:
                return prev
            next_node, node.next = node.next, prev
            return reverse(next_node, node)
            
        return reverse(head, None)