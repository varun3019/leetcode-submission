class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        n=len(nums)
        l,r=0,0
        zero=0
        while r<n:
            if nums[r]==0:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

        
                
        


        