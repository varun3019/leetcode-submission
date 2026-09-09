class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(len(strs[0])):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans

        