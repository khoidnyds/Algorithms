import math
import random
import numpy as np
import time
import sys
from tqdm import tqdm
import os.path
from os import path
import pandas as pd
import matplotlib.pyplot as plt


def SelectionSort(numbers):
    # O(n^2)
    for i in range(len(numbers)-1):
        min_idx = numbers.index(min(numbers[i:]))
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def MergeSort(numbers):
    # O(n*log n)
    if len(numbers) == 1:
        return numbers
    mid = math.floor(len(numbers)/2)

    first = MergeSort(numbers[:mid])
    second = MergeSort(numbers[mid:])

    result = []
    while len(first) and len(second):
        if first[0] <= second[0]:
            result.append(first[0])
            first.pop(0)
        else:
            result.append(second[0])
            second.pop(0)
    if len(first):
        result.extend(first)
    if len(second):
        result.extend(second)
    return result


def QuickSort(numbers):
    # O(n*log n)
    if len(numbers) == 1 or len(numbers) == 0:
        return numbers

    pivot = random.choice(numbers)
    small = QuickSort([x for x in numbers if x < pivot])
    large = QuickSort([x for x in numbers if x > pivot])
    small.extend([pivot])
    small.extend(large)
    return small


def main():
    numbers = [7, 92, 87, 1, 4, 3, 2, 6]
    print("Sorting Problem")
    print("0. Graph complexity")
    print("1. Selection Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    while(1):
        algo = int(input())
        if algo == 1:
            start_time = time.time()
            result = SelectionSort(numbers)
            interval = time.time() - start_time
            print(f'Naive: {result} takes {interval:.5f} seconds')
        elif algo == 2:
            start_time = time.time()
            result = MergeSort(numbers)
            interval = time.time() - start_time
            print(f'Brute Force: {result} takes {interval:.5f} seconds')
        elif algo == 3:
            start_time = time.time()
            result = QuickSort(numbers)
            interval = time.time() - start_time
            print(f'Recursion: {result} takes {interval:.5f} seconds')
        elif algo == 0:
            start, end = 10000, 1000000
            if not path.exists("sort_data.csv"):
                data = []
                for idx in range(3):
                    data_temp = []
                    for r in tqdm(range(start, end, 5000)):
                        numbers = []
                        random.seed(time.time())
                        # generate some integers
                        for _ in range(r):
                            numbers.append(random.randint(0, sys.maxsize))
                        if len(data_temp) and data_temp[-1] > 5:
                            continue
                        start_time = time.time()
                        if idx == 0:
                            result = SelectionSort(numbers)
                        elif idx == 1:
                            result = MergeSort(numbers)
                        elif idx == 2:
                            result = QuickSort(numbers)
                        interval = time.time() - start_time
                        data_temp.append(interval)
                    data.append(data_temp)

                pd.DataFrame(data).to_csv(
                    "sort_data.csv", index=False, header=False)
            else:
                data = pd.read_csv("sort_data.csv",
                                   header=None).values.tolist()
            plt.figure(dpi=1200)
            plt.scatter(np.linspace(start, start+len(data[0])*5000, len(data[0])), data[0],
                        marker='.', color="red", label='Selection Sort')
            plt.scatter(np.linspace(start, start+len(data[1])*5000, len(data[1])), data[1],
                        marker='.', color="green", label='Merge Sort')
            plt.scatter(np.linspace(start, start+len(data[2])*5000, len(data[2])), data[2],
                        marker='.', color="blue", label='Quick Sort')
            plt.legend()
            plt.title("Time Complexity")
            plt.xlabel("Input size")
            plt.ylabel("Seconds")
            plt.savefig('sorting.png')
        else:
            return


if __name__ == "__main__":
    main()
