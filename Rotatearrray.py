while k:
     temp= nums.pop()
     nums.insert(0,temp)
     k-=1
     return nums