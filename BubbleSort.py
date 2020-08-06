def bubble_sort_swaps(nums): #n = 4
  count = 0
  swapped = True
  indexOfLastSorted = len(nums)
  while swapped:
    swapped = False
    for i in range(indexOfLastSorted):
      count+=1
      if i+1 < len(nums):
        if nums[i] > nums[i+1]:
          nums[i],nums[i+1] = nums[i+1],nums[i] #swaps both values
          swapped = True
          
      indexOfLastSorted -= 1
  return nums, "number of iterations: "+str(count)
  

