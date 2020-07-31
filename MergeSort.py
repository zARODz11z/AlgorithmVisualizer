def merge_sort(nums):
  if len(nums) > 1:
    #bisect the list [1,2,3,4,5]
    #                 0 1 2 3 4 
    #create two lists, one for the right half, one for the left half
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    right = merge_sort(right)
    left = merge_sort(left)
    #these lists are now sorted
    #until at least 1 list is empty
      #check the head elem of both lists
        #append the smaller element of the sorted list 
    #concatenate the rest of the other list
    
    sorted_lists = sortLists(left, right)
    # merge the sorted lists
    return sorted_lists
  else: 
    return nums

def sortLists(list1, list2):
  listToReturn = []
  
  while len(list1) > 0 and len(list2) > 0:
    if list1[0] <= list2[0]:
      listToReturn.append(list1.pop(0))
    elif list1[0] >= list2[0]:
      listToReturn.append(list2.pop(0))
      
  
  listToReturn.extend(list1)
  listToReturn.extend(list2)

  return listToReturn