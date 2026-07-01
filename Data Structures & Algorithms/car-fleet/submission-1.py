class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tarspeed = [[position[i],speed[i]] for i in range(len(speed))]
        tarspeed.sort(reverse=True)
        time = []
        for p,s in tarspeed:
            time.append((target-p)/s)

        stack = []
        count = 0
        for t in time:
            if not stack:
                stack.append(t)
            if stack[-1]<t:
                stack.append(t)

        return len(stack)