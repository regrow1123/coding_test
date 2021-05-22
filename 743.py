class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        for u, v, w in times:
            g[u].append([v, w])
        
        dist = {i: float('inf') for i in range(1, n+1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            
            dist[node] = elapsed
            for dest, time in sorted(g[node], key=lambda x: x[1]):
                dfs(dest, elapsed+time)
            
        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1