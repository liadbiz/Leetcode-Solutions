#!/usr/bin/env python
# -*- coding: utf-8 -*-

def shell_sort(arr):
    n = len(arr)
    # hand made sequence 
    gaps = []
    ns = n
    while ns > 1:
        gaps.append(ns // 2)
        ns //= 2
    # or use Marcin Ciura's gap sequence
    # gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    print("here")
    print(gaps)
    for gap in gaps:
        i = gap
        while i < n:
            temp = arr[i]  
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            i += 1
    return arr


if __name__ == "__main__":
    arr = [2, 1, 3, 5, 4]
    print(shell_sort(arr))
