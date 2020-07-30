def bubble_sort_swaps(nums): #n = 4
  count = 0
  swapped = True
  last_unsorted_index = len(nums) 
  
  while swapped:
    swapped = False
    for index in range(last_unsorted_index):
      if index + 1 < len(nums):
        if nums[index] > nums[index+1]:
          nums[index], nums[index+1] = nums[index+1], nums[index]
          count += 1
          swapped = True
          
    last_unsorted_index -= 1
          
  return count
  

#worst case its in decending order
# [6,4,3,2] n = 4
# [4,6,3,2] 1 swap 
# [4,3,6,2] 2 swaps
# [4,3,2,6] 3 swaps 4 elems looked at | n elems
# [3,4,2,6] 4 swaps 
# [3,2,4,6] 5 swaps 3 elems looked at | n-1 elems
# [2,3,4,6] 6 swaps 2 elms looked at | n-2 elems