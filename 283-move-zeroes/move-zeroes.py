class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroarr=[]
        nonzeroarr=[]
        for num in nums:
            if num==0:
                zeroarr.append(num)
            else:
                nonzeroarr.append(num)
        nums[:]=nonzeroarr + zeroarr
        return nums


        