class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
            
        self.least = float('inf')
        q = deque([(0, 0)])
        visited = set([0])

        while q:
            current_sum, count = q.popleft()
            
            for square in squares:
                next_sum = current_sum + square
                if next_sum == n:
                    return count + 1
                if next_sum > n:
                    break
                if next_sum not in visited:
                    visited.add(next_sum)
                    q.append((next_sum, count + 1))
                    
        return -1