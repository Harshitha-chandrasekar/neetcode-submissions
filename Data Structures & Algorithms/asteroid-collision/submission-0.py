class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1,len(asteroids)):
            k = asteroids[i]
            while stack and k < 0 and stack[-1] > 0:
                if abs(k)>stack[-1]:
                    stack.pop()
                    continue
                elif abs(k)==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(k)

        return stack
