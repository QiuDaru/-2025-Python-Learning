class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,int(n)):
         if  "0" not in str(int(n) - i) and"0" not in str(i):
            return i,int(n)-i