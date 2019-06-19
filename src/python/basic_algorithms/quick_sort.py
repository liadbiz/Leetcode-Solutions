#!/usr/bin/env python
# -*- coding: utf-8 -*-
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 5]
    print(quick_sort(arr))
    
