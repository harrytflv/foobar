## Problem

Given integer n and k where 0 <= k <= n, return n arrays of integers satisfying:
* Any combination of k arrays has all integers from 0 to M, where M is the maximum value of all integers in the returned n arrays.
* Any combination of k-1 or less arrays is missing some integers from 0 to M.
* M is as small as possible.
* n arrays are lexicographically least.

## Inspiration

This question feels like a secret sharing problem. And I got the inspiration from the trivial secret sharing solution in https://en.wikipedia.org/w/index.php?title=Secret_sharing.

## Solution

Let n=5 and k=4. We have five bunnies. Name them A, B, C, D, and E. And now we take A, B and C. The key distribution scheme requires that the combination of A, B, and C is missing something that the combination of A, B, C, and D or the combination of A, B, C, and E has. What is it? Apparently, in comparison the the latter combinations, the combination of A, B and C is missing D and E. Now, here comes the core of both the problem and the solution: what exactly is this concept of missing D and E? How to describe it mathematically?

My thinking is that with only A, B and C, nobody is in the combination of D and E. Generally speaking, with k-1 bunnies, nobody is in the combination of the rest n-k+1 bunnies. To find a key disctribution scheme, we assign a number for each combination of n-k+1 bunnies. For bunny i, it will hold key j if only it is in combination j. Given k-1 bunnies, the fact that nobunny is in the combination of the rest n-k+1 bunnies means that this bunny combination is missing the number j representing the rest n-k+1 bunnies combination. However, given k bunnies, all n-k+1 bunnies combination will have some representative. Requirement met.
