class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s = list(s)
        ans = {}
        try1 = []
        for g in range(len(s)):
            for i in s[g : len(s)]:
                if i not in try1:
        
                    try1.append(i)   
           
                else:
                    ans[tuple(try1)] = len(try1)
                    break
            ans[tuple(try1)] = len(try1)
            try1 = []
        return(max(list(ans.values())))