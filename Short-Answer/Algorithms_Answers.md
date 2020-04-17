#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The while will run n * n * n times so as n gets bigger, the operations increase - that reduces to just n. Inside of the while loop is multiplication, which doesn't increase based on n.


b) O(n log(n)) Classic nested loop for loop runs "n" times, incrementing the index by 1 for each iteration through the loop. The while loop doubles "j" every iteration, giving us the run time of O(n log (n))


c) O(n) Because it recurses upon itself, it is a loop, the reason is because bunnies increase the number of recursions increase which puts the recursive loop at O(n). (Despite the recursion, all the operations are done in constant time)

## Exercise II

I would use a binary search method. It starts off at floor f/2 If the egg is broken, It returns the current floor (f/2) else It Repeats this proccess (current floor + (current floot/2)) until It reaches the floor. 

Time complexity: O(log n)
        Because of the binary search method, Divide and conquer
