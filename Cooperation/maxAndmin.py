#coding=utf-8
__author__ = 'zjutK'
def findmax(arr):
    max, index = arr[0], 0
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i];
            index = i;
    return index;


def findmin(arr):
    min, index = arr[0], 0;
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i];
            index = i;
    return index;

