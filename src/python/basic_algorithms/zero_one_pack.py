#!/usr/bin/env python
# -*- coding: utf-8 -*-

def zeroOneKnapsack(C, W, V):
    """0-1 knapsack problem solution

    solve the 0-1 knapsack problem: given of N goods with weight and value for 
    each good that are stored in W and V, select goods and put them into a 
    knapsack with capacity C, find the maximum total value you can get.

    Args:
        C: capacity of knapsack
        W: weights of goods
        V: values of goods

    Returns:
        maximum value you can get
    """
    assert len(W) != 0, "length of W should not be zero"
    assert len(W) == len(V), "lenth of W and length of V should be the same"
    N = len(W)
    dp = [0 for _ in range(C+1)]
    for i in range(N):
        for c in range(C, W[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - W[i]] + V[i])
    print(dp)
    return dp[-1]


if __name__ == "__main__":
    C = 15
    W = [3,2,6,7,1,4,9,5]
    V = [6,3,5,8,3,1,6,9]
    print(zeroOneKnapsack(C, W, V))
