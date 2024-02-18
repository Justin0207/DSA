# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:44:12 2024

@author: HP
"""

def bubble_sort(nums):
    for i in nums:
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)
    return nums

def swap(lis, a, b):
    lis[a], lis[b] = lis[b], lis[a]
    
def merge_sort(nums):
    if len(nums) == 1:
        return 
    mid = len(nums)//2
    left_half = nums[:mid]
    right_half = nums[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1  
        
            
    
    
a = [9, 4,5, 7, 3, 2, 1]
merge_sort(a)
print(a)