class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l=len(nums)
        majority=l/2
        hashset={}
        for n in nums:
            hashset[n]=hashset.get(n,0)+1
            if hashset.get(n)>majority:
                return n
        
        
        
        
        