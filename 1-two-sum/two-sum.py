class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            hintvalue=target-nums[i]
            if hintvalue in hashMap:
                return [i,hashMap[hintvalue]]
            else:
                hashMap[nums[i]]=i
        

        