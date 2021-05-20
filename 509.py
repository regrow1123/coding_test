class Solution:
    def fib(self, n: int) -> int:
        self.cache = {0:0, 1:1}
        
        def memoize(n):
            if n in self.cache:
                return self.cache[n]
            
            self.cache[n] = memoize(n-1) + memoize(n-2)
            return self.cache[n]
        
        return memoize(n)