## Solution

Dynanmic programming.

Subproblem to solve:
Find the number of staircase of using i blocks with height no higher than j.

Transition:
The number of staircase of using i blocks with height no higher than j is the sum of:
1. The number of staircase of using i blocks with height no higher than j-1, which is a solved subproblem
2. The number of staircase of using i blocks with height equal to j. This is the same value as The number of staircase of using i-j blocks with height no higher than j-1, which is again a solved subproblem. A special case is when i-j < j, there is an extra staircase with all i-j blocks  stacked together.
