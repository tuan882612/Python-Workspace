import collections as col, math as m,numpy as np, sys, os, typing

def func(nums, target):
    #hashtable
    # myDict = {}
    # for i, num in enumerate(list):
    #     m = target - num
    #     if m in myDict:
    #         return [myDict[m], i]
    #     else:
    #         myDict[num] = i
    
    #two pointer method
    nums, indexes = zip(*sorted((n, i+1) for i, n in enumerate(nums)))
    return indexes
    # start, end = 0, len(nums)-1
    # while start<end:
    #     m = nums[start]+nums[end]
    #     if m == target:
    #         return [indexes[start], indexes[end]]
    #     elif m > target:
    #         end-=1
    #     else:
    #         start+=1
            
arr = [3,2,4]
tar = 6
print(func(arr, tar))