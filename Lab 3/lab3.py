import random
#import pandas as pd
#import pylab as pl
#import numpy as np
import time
import math
#import matplotlib.pyplot as plt

def MergeSort(ar, start, end):
  if(start<end):
    mid = (start+end)/2
    mid = int(mid)
    MergeSort(ar, start, mid)
    MergeSort(ar, mid+1, end)
    Merge(ar, start, mid, end)

def Merge(ar, start, mid, end):
  p = start
  q = mid+1
  temp = []
  for i in range(0,end-start+1):
    if p>mid :
      temp.append(ar[q])
      q += 1
    elif q>end :
      temp.append(ar[p])
      p += 1
    elif ar[p] > ar[q]:
      temp.append(ar[q])
      q += 1
    else:
      temp.append(ar[p])
      p += 1
  i = 0
  for q in range(start, end+1):
    ar[q] = temp[i]
    i += 1


def insertion_sort(collection, start, end):
    for loop_index in range(start, end+1):
        insertion_index = loop_index
        while insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]:
            collection[insertion_index], collection[insertion_index - 1] = collection[insertion_index - 1], collection[insertion_index]
            insertion_index -= 1

def Merge_insert_Sort(ar, start, end, S):
  if(end-start > S):
    mid = (start+end)/2
    mid = int(mid)
    Merge_insert_Sort(ar, start, mid, S)
    Merge_insert_Sort(ar, mid+1, end, S)
    Merge(ar, start, mid, end)
  else:
    insertion_sort(ar, start, end)

numbers = []
for i in range(1000000):
    numbers.append(random.randint(0,1000))
merge_values = []
insert_values = []
points = []
for z in range(100):
    yeet = []
    huha = []
    k = z
    for i in range(k):
        x = numbers[i]
        yeet.append(x)
        huha.append(x)
    #print("Size: ", k)
    start_time = time.time()
    MergeSort(yeet, 0, len(yeet) - 1)
    time_taken_1 = time.time() - start_time
    #print(yeet)
    #print("Time taken for merge sort = ", time_taken_1*1000)

    start_time = time.time()
    insertion_sort(huha, 1, len(huha)-1)
    time_taken_2 = time.time() - start_time
    #print(huha)
    #print("Time taken in insertion sort = ", time_taken_2*1000)
    merge_values.append(time_taken_1)
    insert_values.append(time_taken_2)
    points.append(k)
    #if(time_taken_1<time_taken_2):
    #    print("Maximum size of array for which insertion sort is faster: ", z-1)
    #    break
    #size = size*10
'''
plt.plot(points, merge_values, label = "MergeSort")
plt.plot(points, insert_values, label = "InsertSort")
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Time analysis for sorting")
plt.legend()
plt.show()
'''
anomalies = []
attempts = 5
for i in range(len(merge_values)):
  if(merge_values[i]<insert_values[i]):
    print(points[i])
    attempts -= 1
    anomalies.append(points[i])
  if(attempts==0):
    break
temp = 1000
for x in range(4):
    print("SIZE ", temp)
    for i in range(len(anomalies)):
        if(anomalies[i] == 1):
            continue
        A = []
        B = []
        for j in range(temp):
            A.append(numbers[i])
            B.append(numbers[i])
        start_time = time.time()
        Merge_insert_Sort(A, 0, len(A) - 1, anomalies[i]-1)
        time_taken_1 = time.time() - start_time
        #print(yeet)
        print("Time taken for Merge(Insert)Sort = ", time_taken_1*1000)

        start_time = time.time()
        MergeSort(B, 0, len(B)-1)
        time_taken_2 = time.time() - start_time
        #print(amigo)
        print("Time taken for MergeSort = ", time_taken_2*1000)
    temp *= 10
