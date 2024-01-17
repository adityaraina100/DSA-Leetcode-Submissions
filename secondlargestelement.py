class Solution:
 
    def print2largest(self,arr, n):
    # code here
        a=list(set(arr))
        a.sort()
         
        if len(a)>1:
            return a[-2]
        return -1
