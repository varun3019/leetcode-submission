class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort() #sort to keep most minimum number in array at starting
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-nums[i]
                k-=1
        if k%2==1:
            min_index=nums.index(min(nums))
            nums[min_index]=-nums[min_index]
        return sum(nums)

        