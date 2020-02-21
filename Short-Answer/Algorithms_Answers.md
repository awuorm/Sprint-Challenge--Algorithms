#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    a = 0  O(1)
    while (a < n * n * n): O(n)
    a = a + n * n O(1)

    Total = O(2) + O(n) => O(n)

b) 
     sum = 0 O(1)
    for i in range(n): O(n^2)
      j = 1 O(1)
      while j < n:
        j *= 2 O(1)
        sum += 1 O(1)

       Total = O(4) + O(n^2) => O(n^2) 

c)
    def bunnyEars(bunnies): O(n)
      if bunnies == 0: O(1) 
        return 0 O(1)

      return 2 + bunnyEars(bunnies-1)  O(n)  

      Total = O(2n) + + O(2) => O(n)

## Exercise II
    1. Define a function that takes 2 inputs. n - number of storeys in the building, f - a default argument that specifies the floor number where eggs start to break if dropped.
    2. Define the base case. If n < f, then append the value 'dropped' to an initialized array 'eggs'.
    3. Else recursively call the helper function
    4. The helper function will have a loop that appends the word 'broken' to 'eggs'.
    5. Subtract the value of 'broken' items in array from 'dropped' items. The value will be the floor number with the least amount of dropped + broken eggs


