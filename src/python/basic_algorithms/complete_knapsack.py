#!/usr/bin/env python
# -*- coding: utf-8 -*-

def completeKnapsack(C, W, V):
    """complete knapsack problem solution

    solve the 0-1 knapsack problem: given of N items with weight and value for 
    each item that are stored in W and V, select items and put them into a 
    knapsack with capacity C, find the maximum total value you can get.

    diffrence with 0-1 knapsack problem: each item can be selected by any times

    Args:
        C: capacity of knapsack
        W: weights of items
        V: values of items

    Returns:
        maximum value you can get
    """
    assert len(W) != 0, "length of W should not be zero"
    assert len(W) == len(V), "lenth of W and length of V should be the same"

    N = len(W)
    dp = [0 for _ in range(C+1)]

    for i in range(N):
        for c in range(W[i], C + 1):
            dp[c] = max(dp[c], dp[c - W[i]] + V[i])

    return dp[-1]


if __name__ == "__main__":
    C = 15
    W = [3,2,6,7,1,4,9,5]
    V = [6,3,5,8,3,1,6,9]
    print(completeKnapsack(C, W, V))
