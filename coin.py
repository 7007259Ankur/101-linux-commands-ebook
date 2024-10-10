# A Naive recursive python program to find minimum of coins
# to make a given change sum

import sys

# m is size of coins array (number of different coins)
def minCoins(coins, m, sum):

    # base case
    if (sum == 0):
        return 0

    # Initialize result
    res = sys.maxsize
    
    # Try every coin that has smaller value than sum
    for i in range(0, m):
        if (coins[i] <= sum):
            sub_res = minCoins(coins, m, sum-coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res

# Driver program to test above function
coins = [9, 6, 5, 1]
m = len(coins)
sum = 11
print("Minimum coins required is",minCoins(coins, m, sum))

# This code is contributed by
# Smitha Dinesh Semwal
