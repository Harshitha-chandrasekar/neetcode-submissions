class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0,len(numbers) - 1
        sum = numbers[index1] + numbers[index2]
        while index1 <  index2:
            sum = numbers[index1] + numbers[index2]

            if sum < target:
                index1 = index1 + 1
            elif sum > target:
                index2 = index2 - 1
            else:
                return [index1+1,index2+1]


        return [index1+1, index2+1]
