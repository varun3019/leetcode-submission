class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        newarr=[]
        while(i<m and j<n):
            if(nums1[i]<nums2[j]):
                newarr.append(nums1[i])
                i+=1
            else:
                newarr.append(nums2[j])
                j+=1
        while(i<m):
            newarr.append(nums1[i])
            i+=1
        while(j<n):
            newarr.append(nums2[j])
            j+=1
        nums1[:]=newarr
        
        