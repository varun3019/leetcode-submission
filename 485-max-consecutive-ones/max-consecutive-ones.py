class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        maxone=0
        for num in nums:
            if num==1:
                count+=1
                maxone=max(maxone,count)
            elif num==0:
                count=0
        return maxone
            

        
        