class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float("-inf")
        sumed=0
        for num in nums:
            sumed+=num
            maxi=max(maxi,sumed)
            if sumed<0:
                sumed=0
        return maxi
        