import math
import time
import sys
import copy
import numpy as np
from itertools import permutations, product
from collections import defaultdict
import matplotlib.pyplot as plt
from tqdm import tqdm
import csv
import os.path
from os import path
import pandas as pd


def GreedyChange(money, coins):
    if money in coins:
        return {money: 1}

    remain = money
    result = {}
    for coin in coins:
        count = math.floor(remain/coin)
        remain -= count*coin
        if count > 0:
            result[coin] = count

    return sorted(result.items(), reverse=True)


def BruteForceChange(money, coins):
    # time:  O(len(coins)^(money/min(coins))) ~ O(m^n)
    # space: O(m^n)
    if money in coins:
        return {money: 1}

    coins = [x for x in coins if x < money]
    smallest_num_coins = sys.maxsize
    result = {}

    max_count = np.floor(np.divide(money, np.array(coins)))
    max_count = max_count.astype('int32')
    # passing a list as multi-parameters!
    pers = product(*[range(max_count[i]+1) for i in range(len(coins))])

    for per in pers:
        total = 0
        for p, d in zip(per, coins):
            total += p*d
        if total == money:
            if np.sum(per) < smallest_num_coins:
                smallest_num_coins = np.sum(per)
                result = {coins[i]: per[i]
                          for i in range(len(coins)) if per[i] != 0}

    return result


def RecursiveChange(money, coins):
    # time:  O(len(coins)^(money/min(coins))) ~ O(m^n)
    # space: 1
    if money == 0:
        return []

    num_coins = sys.maxsize
    result = []
    for coin in coins:
        if money >= coin:
            used_coins = RecursiveChange(money - coin, coins)

            num_coin = len(used_coins) + 1
            used_coins.append(coin)

            if num_coin < num_coins:
                result = used_coins
                num_coins = num_coin
    return result


def DynamicProgrammingChange(money, coins):
    # time:  O(len(coins)*(money/min(coins))) ~ O(mn)
    dp = {0: []}
    for i in range(1, money+1):
        num_coins = sys.maxsize
        num_list = []
        for coin in coins:
            if coin <= i:
                pre_num_coins_1 = len(dp[i-coin])+1
                pre_list_coins = copy.deepcopy(dp[i-coin])
                if pre_num_coins_1 < num_coins:
                    num_coins = pre_num_coins_1
                    pre_list_coins.append(coin)
                    num_list = copy.deepcopy(pre_list_coins)
        dp[i] = num_list

    return dp[money]


money = 48
coins = [120, 40, 24, 5, 1]


def main():
    print("Money Change Problem")
    print("0. Graph complexity")
    print("1. Greedy")
    print("2. Brute Force")
    print("3. Recursion")
    print("4. Dynamic Programming")
    while(1):
        algo = int(input())
        if algo == 1:
            start_time = time.time()
            result = GreedyChange(money, coins)
            interval = time.time() - start_time
            print(f'Naive: {result} takes {interval:.5f} seconds')
        elif algo == 2:
            start_time = time.time()
            result = BruteForceChange(money, coins)
            interval = time.time() - start_time
            print(f'Brute Force: {result} takes {interval:.5f} seconds')
        elif algo == 3:
            start_time = time.time()
            result = RecursiveChange(money, coins)
            interval = time.time() - start_time
            print(f'Recursion: {result} takes {interval:.5f} seconds')
        elif algo == 4:
            start_time = time.time()
            result = DynamicProgrammingChange(money, coins)
            interval = time.time() - start_time
            print(
                f'Dynamic Programming: {result} takes {interval:.5f} seconds')
        elif algo == 0:
            start, end = 20, 500
            if not path.exists("change_data.csv"):
                data = []
                coins = [120, 40, 24, 5, 1]
                for idx in range(3):
                    data_temp = []
                    for money in tqdm(range(start, end)):
                        if len(data_temp) and data_temp[-1] > 5:
                            continue
                        start_time = time.time()
                        if idx == 0:
                            result = BruteForceChange(money, coins)
                        elif idx == 1:
                            result = RecursiveChange(money, coins)
                        elif idx == 2:
                            result = DynamicProgrammingChange(money, coins)
                        interval = time.time() - start_time
                        data_temp.append(interval)
                    data.append(data_temp)

                pd.DataFrame(data).to_csv(
                    "change_data.csv", index=False, header=False)
            else:
                data = pd.read_csv("change_data.csv",
                                   header=None).values.tolist()
            plt.figure(dpi=1200)
            plt.scatter(np.linspace(start, start+len(data[0]), len(data[0])), data[0],
                        marker='.', color="red", label='Brute Force')
            plt.scatter(np.linspace(start, start+len(data[1]), len(data[1])), data[1],
                        marker='.', color="green", label='Recursive')
            plt.scatter(np.linspace(start, start+len(data[2]), len(data[2])), data[2],
                        marker='.', color="blue", label='Dynamic Programming')
            plt.legend()
            plt.title("Time Complexity")
            plt.xlabel("Money")
            plt.ylabel("Seconds")
            plt.savefig('changing.png')
            plt.show()
        else:
            return


if __name__ == "__main__":
    main()
