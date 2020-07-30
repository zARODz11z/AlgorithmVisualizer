def bubble_sort_swaps(nums): #n = 4
  count = 0
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums)):
      count+=1
      if i+1 < len(nums):
        if nums[i] > nums[i+1]:
          nums[i],nums[i+1] = nums[i+1],nums[i] #swaps both values
          swapped = True
  return nums, "number of iterations: "+str(count)
  

