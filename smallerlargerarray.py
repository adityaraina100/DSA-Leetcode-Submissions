Class Solution:	
def getMoreAndLess(self,arr, n, x):
        greater = lesser = 0
        for i in arr:
            if i >= x:
                greater += 1
            if i <= x:
                lesser +=1
        return lesser, greater