#### Binary search is a faster 🏃💨 way of searching for something. There are a few conditions though, the data structure has to be sorted. Take a look at the example 

    Given [2,3,5,6,8,10,12,15,19] Target = 15
    index: 0 1 2 3 4  5  6  7  8
           ^       ^           ^
          low     mid        high 
      1) We keep 3 pointers, low, mid, high at the indices 

      2) Mid is calculated by taking (low + high)//2 which truncates the decimal because of integer division.In our example (0+8)//2 = 4
      
      💡OR Mid can be safely calculated by 
      mid = low + ((high-low)//2)💡


      this accounts for integer overflow, the previous version does not account for if our low + high was bigger than the biggest possible int allowed in python. For more info read this blog.
      https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html


      3) Now that we calculated our middle point, we check if the middle point is less than, greater than or if that is our target. 
      We can disregaurd half of the list if target is greater or less than the mid by reassigning low or high respectively. 

      4) Keep calculating mid and checking if you found the target. Or your low == high then you reached the end of the list

#### TIME & SPACE COMPLEXITY:🤔
*Big O Notation describes how your algorithm scales when your input size becomes huge.
*Your main concern is the worst case scenario. In the worst case scenario how will your algorithm grow in the number of steps(time) and space used.

Say were Given arr=[2,3,4,5,6,7,8,9] with target = -2
**arr has 8 elements so well say n=8**
**1st iteration**
[2,3,4,5,6,7,8,9] Target = -2
 0 1 2 3 4 5 6 7 indices
 L     M       H 
 mid value=5 and 5 > -2 so disregard right side by reassigning the High pointer to mid-1

**2nd iteration**
[2,3,4,5,6,7,8,9] Target = -2
 0 1 2 3 4 5 6 7 indices
 L M H 
 mid value=3 and 3 > -2 so disregard right side by reassigning the High pointer to mid-1

**3rd iteration**
[2,3,4,5,6,7,8,9] Target = -2
 0 1 2 3 4 5 6 7 indices
 L
 H
 M

 mid value=2 and 2 > -2 and we've reached the end of the list since Low=High

 In this case We did 3 iterations and did not find our element.
 So given N=8 elements we took 3 iterations in the worst case scenario of the element not being in the list. 

 log(8) with a base of 2 equals 3 so we can describe our algorithm as being O(log(n)) because in the worst case we take log(n) steps where n is our input size. 

 "This algorithm runs in O(log(n)) with respect to the input size n."





      
       

"""