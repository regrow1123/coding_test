# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        values.sort()
        node = head
        for value in values:
            node.val = value
            node = node.next
        
        return head