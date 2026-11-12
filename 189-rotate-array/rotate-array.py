class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        n=len(nums)
        k=k%n
        for i in range(n-k,n):
            temp.append(nums[i])
        for i in range(n-k):
            temp.append(nums[i])
        nums[:]=temp
        return nums
        