class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi=mini=result=nums[0]
        for num in nums[1:]:
            if num<0:
                maxi,mini=mini,maxi
            maxi=max(num,maxi*num)
            mini=min(num,mini*num)
            result=max(maxi,result)
        return result