#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    list1=[]
    for i in range(n):
        list1.append(i)
    flag=0
    sum=0
    #print(n)
    for i in range(0,n):
        b=q.index(i+1)
        r=i-b
        list2=[-2,2,-1,0,1]
        if r in list2:
            flag=flag+1
            sum=sum+abs(r)
    
    if flag==(n):
        print(sum//2)
    else:
        print("Too chaotic")
            
            
        
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
