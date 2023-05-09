import random

def getIntList(length, min, max):
    lista = [random.randint(min, max) for int in range(length)]
    return lista

def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def selectionSort(list):
    for i in range(len(list)):
        min= i
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list


def insertionSort(list):
    for i in range(1, len(list)):
        aux = list[i]
        j = i-1
        while j >= 0 and aux < list[j] :
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = aux
    return list

def shellSort(list):
    gap=len(list)//2
    while gap>0:
        j=gap
        while j<len(list):
            i=j-gap
            while i>=0:
                if list[i+gap]>list[i]:
                    break
                else:
                    list[i+gap],list[i]=list[i],list[i+gap]
                i=i-gap
                j+=1
        gap=gap//2
    return list


def mergeSort(list):
    if len(list) > 1:
        centre = len(list)//2
        left = list[:centre]
        right = list[centre:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


def partition(list, low, high):

    pivot = list[high]

    i = low - 1

    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
    (list[i + 1], list[high]) = (list[high], list[i + 1])
    return i + 1


def quickSort(list, low, high):
    if low < high:
        pi = partition(list, low, high)
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)
    return list

#%%
import time
def cron35(alg):
    lst = list()
    for n in range(35):
        i1 = time.time()
        alg
        f1 = time.time()
        t1 = f1 - i1
        lst.append(t1)
    return lst

import time

def tryThisFunc(func, ord, n , max, num):
    times = list()
    for i in range(num):
        arr = ord(n,max)
        start = time.time()
        func(arr)
        end = time.time()
        times.append(end -start)
    return times


def media(alg):
    return sum(cron35(alg))/len(cron35(alg))

lista = getIntList(10000, 0, 100000)
print("Initial List: ")
print(lista)

print("bubbleSort: ")
print(media(bubbleSort(lista)))
print(cron35(bubbleSort(lista)))

#print("bubbleSort: ")
#print(bubbleSort(list))
print("selection sort: ")
print(media(selectionSort(lista)))
print(cron35(selectionSort(lista)))
#print(selectionSort(list))
#print("Insertion Sort:")
#print(insertionSort(list))
#print("Quick Sort:")
#print(quickSort(list,0,(len(list)-1)))

print("bubbleSort: ")
print(cron35(bubbleSort, lista))
print("Selection Sort: ")
print(cron35(selectionSort, lista))
print("Insertion Sort:")
print(cron35(insertionSort, lista))
print("Shell Sort:")
print(cron35(shellSort, lista))
print("Merge Sort:")
print(cron35(mergeSort, lista))
print("Quick Sort:")
print(cron35(quickSort, lista))