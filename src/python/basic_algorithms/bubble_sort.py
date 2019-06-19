#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 一共只需要迭代n - 1
        swapped = False    
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped: # 如果某一轮迭代没有交换元素，说明排序提前完成
            break
    return arr


if __name__ == "__main__":
    arr = [3,1,2,4,5]
    print(bubble_sort(arr))

