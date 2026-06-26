class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,low,mid,high):
            n1 = arr[low:mid+1]
            n2 = arr[mid+1:high+1]
            ans = []
            l1 = len(n1)
            l2 = len(n2)
            i = 0
            j = 0
            while i<l1 and j<l2:
                if n1[i]<=n2[j]:
                    ans.append(n1[i])
                    i = i+1
                else:
                    ans.append(n2[j])
                    j = j+1
            while i<l1:
                ans.append(n1[i])
                i = i+1
            while j<l2:
                ans.append(n2[j])
                j = j+1
            arr[low:high+1] = ans

        def mergesort(arr,low,high):
            if low == high:
                return arr
            mid = (low+high)//2

            mergesort(arr,low,mid)
            mergesort(arr,mid+1,high)
            merge(arr,low,mid,high)
            return arr

        return mergesort(nums,0,len(nums)-1)