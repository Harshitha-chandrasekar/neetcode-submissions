class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #cycle sorted? no but good shot
        if mountainArr.length()<3:
            return -1

        l = 0
        r = mountainArr.length()-1

        while l<r:
            m = (l+r)//2
            if mountainArr.get(m)<mountainArr.get(m+1):
                l = m+1
            else:
                r = m

        peak = l

        #check left half
        l = 0
        r = peak
        while l<=r:
            mid = (l+r)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val<target:
                l = mid+1
            else:
                r = mid-1
        #check right half
        l = peak+1
        r = mountainArr.length()-1
        while l<=r:
            mid = (l+r)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val>target:
                l = mid+1
            else:
                r = mid-1

        return -1