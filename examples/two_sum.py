#Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

def twoSum(stockProfits: List[int], target: int) -> List[int]:

    profits = {}

    for i, price in enumerate(stockProfits):

        profit = target - price

        if profit in profits:
            return [profits[profit], i]

        profits[price] = i


# Example 1:

stockProfits = [2,7,11,15]
target       = 9
# Output: [0,1]
# Explanation: Because nums[0] + stockProfits[1] == 9, we return [0, 1].

# Example 2:
# stockProfits = [3,2,4]
# target = 6
# Output: [1,2]

# Example 3:
# stockProfits = [3,3]
# target = 6
# Output: [0,1]

print(twoSum(stockProfits, target))