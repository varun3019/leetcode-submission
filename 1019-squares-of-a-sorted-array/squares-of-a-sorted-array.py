class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        for j in range(n):
            nums[i]=nums[j]*nums[j]
            i+=1
        return sorted(nums)
        