class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        gas_num = len(gas)
        profit = [gas[i] - cost[i] for i in range(gas_num)]
        if sum(profit) < 0:
            return -1
        
        heap = []
        for i, p in enumerate(profit):
            heapq.heappush(heap, [-p, i])
        
        while True:
            p, i = heapq.heappop(heap)
            total, offset = 0, 0
            while total >= 0:
                total += profit[(i+offset)%gas_num]
                offset += 1
                if offset == gas_num:
                    return i