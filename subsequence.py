class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n1=len(s)
        n2=len(t)
        while i< n1 and j< n2:
                if s[i]==t[j]:
                    i+=1
                elif i==n1:
                    return True
                j+=1
        return True if i==n1 else False