#### Bubble Sort easy but naive way of sorting data. Take a look at the example 

    Given [5,2,3,7] we want it in accending order
    
      1) We compare adjacent elements to see if one is out of order. 

      2) If they are in the wrong order than we swap the values and move to the next element.
            
      3) 💡We know the list is sorted if we go through the list and made no swaps.

      

#### TIME & SPACE COMPLEXITY:🤔
*Big O Notation describes how your algorithm scales when your input size becomes huge.
*Your main concern is the worst case scenario. In the worst case scenario how will your algorithm grow in the number of steps(time) and space used.

Worst case scenario is that our array is in decending order and we want to make it accending
Say were Given arr=[7,5,3] arr has 3 elements so well say n=3
                    ^index
    
**1st iteration**
7 > 5 so swap them
[7,5,3] -> [5,7,3]
 ^index

**2nd iteration**
7 > 3 so swap them
[5,7,3] -> [5,3,7]
   ^index

**3rd iteration **
7 is the end of the list so we just move back to start
[5,3,7]
     ^index

**4th iteration MOVE BACK TO BEGINNING ** 
5 > 3 so swap them
[5,3,7] -> [3,5,7]
 ^index

**5th iteration ** 
5 < 7 so leave it
[3,5,7]
   ^index

**6th iteration** 
7 is the end of the list so we go to the start
[3,5,7]
     ^index

**7th iteration** 
3 < 5 so leave it
[3,5,7]
 ^index

**8th iteration** 
5 < 7 so leave it
[3,5,7]
   ^index

**9th iteration** 
7 is the end of the list and we havent made any swaps this time so the array is sorted
[3,5,7]
     ^index


 In this case We did 9 iterations to sort the array.
 So given N=3 elements we took 9 iterations in the worst case scenario of the array being in decending order. 

 3^2 = 9 so we can describe our algorithm as being O(n^2) because in the worst case we take n^2 steps where n is our input size. 

 "This algorithm runs in O(n^2) with respect to the input size n."

 We could optimize this slightly by not looking at the last element since that one should be sorted by the time we get there but Its not much faster than O(n^2) and other algorithms are much better.





      
       

"""