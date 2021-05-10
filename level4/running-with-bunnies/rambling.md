## Problem

Graph G is a fully-connected directed graph and is given in adjecency matrix, with each edge having a weight. The first vertex in the adjecency matrix is the source and the last is the destination. Given a total weight budget, find a path that can visit the most number of unique vertices so that the total weights of edges along the path is within the budget. Return the visited vertices sorted from low to high. If multiple such path exist, return the one with least vertex indices. Vertices can be revisited.

## Solution

Basically it comes down to brute force every possible path and pick the best one.

One way to enumerate all the paths is similar to the BFS approach in https://leetcode.com/problems/shortest-path-visiting-all-nodes/.

My approach is to use Floyd Warshall algorithm to calculate the shortest distance between each vertices, then think of each permutation of vertices as an order of unique visited vertices. For example, for the path A-B-C-B-D, the order of unique visited vertices corresponds to permutation ABCD. This result of running this algorithm can also be used to check the existence of negative cycles, which means that we can visit all vertices given any time limit. After than, enumerate all permutations with shortest path for each step, we can find the best path that suites the requirement.

## TODO

Prove that this problem is NP-complete. It feels relavant to the Tranvelling Salesman Problem.
