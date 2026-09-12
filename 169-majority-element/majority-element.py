import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)/2
        val=math.ceil(n)
        hashMap={}
        for num in nums:
            hashMap[num]=hashMap.get(num,0)+1
            if hashMap[num]==val:
                return num
        return False
        