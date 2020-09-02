# sortingAlgorithm
develop algorithm concept for algorithm exam
## Sorting Algorithm
 ##  Selection Sort
      step 1 Set minimum value to array[0] aka index = position  | > 0 < | 1 | 2| ....| >
      step 2 search the minimum element in the array
      step 3 swap with value in min variable
      step 4 increment min variable to point to next level  
[selection_sort_code](https://repl.it/@biwanari/ExcitableStarkDeskscan#selectionsort.py)
      
  ## Insertion Sort
      step 1 initialize two index i and j and set i = 1 and j = i-1 < | j | i | | | | | | | | | >
      step 2 declare a variable k where located arr[i]
      step 3 iterate over arr and where k is minus than arr[j] swap them
      step 4 again iterate until all previous number are minus expect arr[k]
      step 5 go ahead and repeat step 2 ~ 4 until array is sorted
[insertion_sort_code](https://repl.it/@biwanari/ExcitableStarkDeskscan#insertionsort.py)
      
  ## Merge Sort
     Mergesort is based on divide and conquer concept, it divides array in two halves,
     calls itself(recursively) for the two halves and then merges the two sorted halves
     
     Let assume we have array -> (38,27,43,3,9,82,10) divide in left part and right part
     Left part -> (38,27,43,3)
     Right part -> (9,82,10)    we divide again in two part until we obtain all singleton part
     
     let assume the final recursive called until the first left part is > 1
                        ____ ____ ____ ___ ___ ____ ____ 
     now the situation | 38 | 27 | 43 | 3 | 9 | 82 | 10 |  where every single i-element are a sub-array
                        ‾‾‾‾ ‾‾‾‾ ‾‾‾‾ ‾‾‾ ‾‾‾ ‾‾‾‾ ‾‾‾‾‾ 
     then we take couple of singleton element as (i, i+1) i.e. (38,27) and sorted it(27,38)
     the we take couple of singleton element as (i',i'+1) i .e .(43,3) and sorted it(3, 43)
     and we obtain
     
                        ____ ____  ____ ___ ___ ____ ____ 
     nwo the situation | 27 | 38 | 3 | 43 | 82 | 9 | 10 |  where every couple of  i-element are a sub-array
                        ‾‾‾‾ ‾‾‾‾ ‾‾‾‾ ‾‾‾ ‾‾‾ ‾‾‾‾ ‾‾‾‾‾
                        
     we can take every single couple and find the minus and then sorted, in other words:
     we take couple number one (27,38)
     we take couple number two (3,43)
     now determinate if 27 > than 3? yes, we swap them
     then we compare 27 and 43: 27 > 43? no, do nothing
     again we compare 38 and 43: again , do nothing
     
     now we can take the last tuple of couple
     we take couple number one (9,82)
     we take couple number two (10)
     compare 9 and 10: 9 > 10  no, so do nothing
     compare 82 and 10: 82 > 10? yes, swap them
     
     now the situtation has changed again, we obtain two big side parts
     
     Left part -> (3,27,38,43)
     Right part -> (9,10,82)    we divide again in two part and come back to big left and right parts
     
     Now we set i = 0 on Left
     and j = 0 on right part
     we compare 3 and 9: 3 < 9? yes put 3 and increment i-index
     then 
     we compare 27 and 9: 27 < 9? no, put 9 after 3 in tmp_array and iterate over right part until n-1(end of array)
     when right part finished take 27 and insert in tmp_array
     repeat on each parts until you ends up the array parts
     at the and we obtain a sorted array
     REMEMBER THIS---> MERGE SORT USE A SUPPORT ARRAY TO ORDER THE ELEMENTS, so is not a "in loco" sorted algorithm
[merge_sort_code]( https://github.com/biwanari/sortingAlgorithm/blob/master/MergeSort.py )
     
     
     
Reference:  
[geekforgeek](https://www.geeksforgeeks.org/)  
(my medium profile)[https://medium.com/@andrewraieta]
