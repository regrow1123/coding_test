# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        hp = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(hp, (head.val, i, head))

        root = node = ListNode(None)

        while hp:
            temp = heapq.heappop(hp)
            node.next = temp[2]
            node = node.next

            if node.next:
                heapq.heappush(hp, (node.next.val, temp[1], node.next))
        
        return root.next