class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        i=0
        j=0
        res=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        if len(neg)==0:
            return [x*x for x in pos]
        if len(pos)==0:
            return [x*x for x in neg][::-1]
        pos=[x*x for x in pos]
        neg=[x*x for x in neg][::-1]
        n,m=len(pos),len(neg)
        while(i<n and j<m):
            if(pos[i]<neg[j]):
                res.append(pos[i])
                i+=1
            else:
                res.append(neg[j])
                j+=1
        while(i<n):
            res.append(pos[i])
            i+=1
        while(j<m):
            res.append(neg[j])
            j+=1
        return res
        