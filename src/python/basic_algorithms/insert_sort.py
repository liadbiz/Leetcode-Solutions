#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

if __name__ == "__main__":
    arr = [2, 1, 3, 5, 4]
    print(insert_sort(arr))

        
