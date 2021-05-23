class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mn=[float('inf')]*n
        mn[src]=0
        
        for k in range(K+1):
            newmn=mn[:]
            for (a,b, cost) in flights:
                newmn[b]=min(newmn[b],mn[a]+cost)
            mn=newmn
            
        return mn[dst] if mn[dst]!=float('inf') else -1