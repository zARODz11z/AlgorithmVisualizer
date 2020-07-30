#binary search that returns true or false if #target is found
#Say were Given arr=[2,3,4,5,6,7,8,9] with target = -2
#**arr has 8 elements so well say n=8**
#**1st iteration**
#[2,3,4,5,6,7,8,9] Target = -2
# 0 1 2 3 4 5 6 7 indices
# L     M       H 
def binarySearch(numsList,target):
  low = 0
  high = len(numsList)-1
  while low < high:
    mid = low + ((high-low)//2)
    if numsList[mid] == target:
      return True
    elif numsList[mid] > target:
      high = mid-1
    elif numsList[mid] < target:
      low = mid+1

  return False
  
