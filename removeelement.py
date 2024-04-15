class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        i=0
        j=0
        while j<len(arr):
            if arr[j]!=val:
                arr[i]=arr[j]
                i+=1
            j+=1
        return i