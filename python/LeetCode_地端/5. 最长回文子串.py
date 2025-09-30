class Solution:
    def longestPalindrome(self, s: str) -> str:

        s2 = s[::-1]
        for i in range(len(s)): #長度
    
            for x in range(i+1):
                s3 = s[0+i-x:len(s)-x:]
                s3 = s3[::-1]
        #print("i=",i,"x=",x)
        #print( s[0+i-x:len(s)-x:],"//",s3 )
                if s[0+i-x:len(s)-x:] == s3:
                    return  s[0+i-x:len(s)-x:] 
