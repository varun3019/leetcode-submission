class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap={}
        n=len(nums)
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for element,count in hashmap.items():
            if count>=n/2:
                return element
        