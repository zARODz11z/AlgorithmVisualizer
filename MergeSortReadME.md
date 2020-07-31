#### Merge Sort: A recursive sort that is Slightly faster than BubbleSort but at the cost of space.

    Given [10,9,8,6] we want it in accending order
    
      1) We split the array in halves all the way until you have 1 element by recursively calling the mergeSort function.

      2) 💡Once the array has been split up into N single arrays then sort those arrays back towards the top.

      It is easier to visualize MergeSort as a tree 
        Split array down to 6 single lists from top to bottom
        height-        [10,9,8,6]                 
          2   |       /        \
              |    [10,9]       [8,6] 4
              |    /   \       /     \
              -  [10]  [9]    [8]   [6] 4 operations
                  \   /        \    /
                  [9,10]      [6,8]
                        \      /
                      [6,8,9,10] Sorted👍
      -------------------------------------------------------
                Sort each sub array from the bottom up
                            


#### TIME & SPACE COMPLEXITY:🤔
*Big O Notation describes how your algorithm scales when your input size becomes huge.
*Your main concern is the worst case scenario. In the worst case scenario how will your algorithm grow in the number of steps(time) and space used.

Worst case scenario is that our array is in decending order and we want to make it accending
Say were Given arr=[10,9,8,6] arr has 4 elements so well say n=4
                    (4*log(4)) = 8

    







      
       

