class Solution:
    def trap(self,arr: List[int]) -> int:
        n= len(arr)
        waterTrapped= 0
        leftmax_ar=[0]*n
        rightmax_ar=[0]*n
        prevmax=0
        for i in range(n):
            leftmax_ar[i]= max(prevmax,arr[i])
            if arr[i]>prevmax:
                prevmax=arr[i]
        prevmax=0
        for i in range(n-1,-1,-1):
            rightmax_ar[i]= max(prevmax,arr[i])
            if arr[i]>prevmax:
                prevmax= arr[i]
        print(leftmax_ar,rightmax_ar,sep="\n")
        for i in range(n):
            j=i
            leftMax=leftmax_ar[i]
            rightMax=rightmax_ar[i]
            waterTrapped+= min(leftMax, rightMax)- arr[i]
        return waterTrapped