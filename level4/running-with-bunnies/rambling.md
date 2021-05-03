## Problem

Graph G is a fully-connected directed graph and is given in adjecency matrix, with each edge having a weight. The first vertex in the adjecency matrix is the source and the last is the destination. Given a total weight budget, find a path that can visit the most number of unique vertices so that the total weights of edges along the path is within the budget. Return the visited vertices sorted from low to high. If multiple such path exist, return the one with least vertex indices. Vertices can be revisited.

## Solution

Basically it comes down to brute force every possible path and pick the best one.

A naive case of this problem is graph with negative cycles, a cycle with negative total weights. If such cycle exists, we can travel as much as needed along the cycle, thus ignoring the weight budget and visit all the vertices. Ask Google about finding negative cycles, and he will tell you a story about Bellman–Ford.

Given the naive case solved, we can assume this graph is free of negative cycles. With that in mind, it is intuitive that one cannot infinitely traverse the graph without breaking the total weight limit. In other words, the number of paths from source to destination is limited. Considering that the size of the graph for this specific problem is relatively small, at this point, we can iterate through all paths from source to destination, compare them and pick our favorite. A special case worthy of notice is zero weight cycle. As we traverse in the graph, we need to implement some validation to prevent us from infinitly looping along zero cycles. In fact, this very same check can be used for detecting negative cycles, 

