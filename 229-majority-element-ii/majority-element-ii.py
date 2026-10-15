from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        newarr=[]
        hashset={}
        n=len(nums)
        for num in nums:
            hashset[num]=hashset.get(num,0)+1
            if hashset[num]>n/3 and num not in newarr:
                newarr.append(num)
        return newarr
        