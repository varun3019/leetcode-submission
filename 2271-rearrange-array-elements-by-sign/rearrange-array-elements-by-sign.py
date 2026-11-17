class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        postive_arr=[]
        negative_arr=[]
        modified_arr=[]
        for num in nums:
            if num>0:
                postive_arr.append(num)
            else:
                negative_arr.append(num)
        for postive,negative in zip(postive_arr,negative_arr):
            modified_arr.append(postive)
            modified_arr.append(negative)
        return modified_arr
        
        
        