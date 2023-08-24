#!/usr/bin/python3
"""
Task: Inner Transformation of Change
Given a collection of coins with different values,
calculate the minimum number of coins required to
reach a specified total amount.

Parameters:
- coins: A list of coin values
- total: The target total amount

Returns:
- The minimum number of coins needed to reach the total
  - Returns 0 if the total is 0 or negative
  - Returns -1 if the total cannot be achieved with available coins

Notes:
- The value of each coin is always a positive integer
- It is assumed that there is an unlimited supply of each denomination

"""

def calculateMinCoins(coins, total):
    """
    Given a collection of coins with different values,
    calculate the minimum number of coins required to
    reach a specified total amount.
    
    Parameters:
    - coins: A list of coin values
    - total: The target total amount
    
    Returns:
    - The minimum number of coins needed to reach the total
      - Returns 0 if the total is 0 or negative
      - Returns -1 if the total cannot be achieved with available coins
    """
    if total <= 0:
        return 0
    
    max_val = total + 1
    coin_counts = {0: 0}
    
    for i in range(1, total + 1):
        coin_counts[i] = max_val
        
        for coin in coins:
            current = i - coin
            if current < 0:
                continue
            
            coin_counts[i] = min(coin_counts[current] + 1, coin_counts[i])
    
    if coin_counts[total] == total + 1:
        return -1
    
    return coin_counts[total]
