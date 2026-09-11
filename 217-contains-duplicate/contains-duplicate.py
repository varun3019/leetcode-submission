class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap={}
        for num in nums:
            hashMap[num]=hashMap.get(num,0)+1
            if hashMap[num]==2:
                return True
        return False

            
        