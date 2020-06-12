#!/bin/python3

import math
import os
import random
import re
import sys

def mostActive(customers):
    n=len(customers)
    l=[]
    dict_c={}
    for i in customers:
        if i in dict_c:
            dict_c[i]+=1
        else:
            dict_c[i]=1
    for i in dict_c:
        return dict_c[i]
        temp=dict_c[i]/n
        if temp>=5:
            l.append(i)
    return l
    # Write your code here


customers_count = int(input().strip())

customers = []
for _ in range(customers_count):
    customers_item = input()
    customers.append(customers_item)

result = mostActive(customers)
print(result)
