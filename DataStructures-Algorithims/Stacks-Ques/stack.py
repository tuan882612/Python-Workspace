import collections as col, math as m,numpy as np, sys, os, typing

def function(s):
        stack = []
        for i in s:
            if i not in stack or not stack:
                stack.append(i)
            else:
                print(stack[-1])
                if stack[-1] < i:
                    stack.pop()
        return stack
    
if __name__ == "__main__":
    arr = ")()())"
    print(function(arr))