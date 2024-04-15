class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        n=len(nums)
        while j<n:
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
            j+=1
        while i<n:
            nums[i]=0
            i+=1