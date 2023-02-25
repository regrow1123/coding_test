class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        path = []
        
        while True:
            cnt = 0
            for task, _ in counter.most_common(n+1):
                cnt += 1
                
                path.append(task)
                counter[task] -= 1
                counter += collections.Counter()
                
            if not counter:
                break
            
            for i in range(n-cnt+1):
                path.append('idle')
        
        return len(path)