class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0:0,1:1,2:1}
        def func(n):
            if n in cache:
                return cache[n]
            cache[n] = func(n-1) + func(n-2) + func(n-3)
            return cache[n]
        
        return func(n)