class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seenno = set(deadends)
        if '0000' in seenno:
            return -1
        
        def children(num):
            res = []
            for i in range(4):
                digit = str((int(num[i])+1)%10)
                res.append(num[:i]+digit+num[i+1:])
                digit = str((int(num[i])+10-1)%10)
                res.append(num[:i]+digit+num[i+1:])
            return res


        q = deque([('0000',0)])
        while q:
            lock,turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in seenno:
                    seenno.add(child)
                    q.append((child,turns+1))

        return -1