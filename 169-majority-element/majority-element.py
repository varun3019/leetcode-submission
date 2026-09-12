import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res=0
        maxcount=0
        n=len(nums)//2
        for num in nums:
            count[num]=count.get(num,0)+1
            res=num if count[num]>maxcount else res
            maxcount=max(maxcount,count[num])
        return res
        