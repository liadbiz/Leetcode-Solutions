#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    def merge(left, right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return result + left + right

    mid = n // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 5]
    print(merge_sort(arr))
