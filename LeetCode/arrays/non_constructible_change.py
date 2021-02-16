def nonConstructibleChange(coins):
    curr_total = 0
    coins.sort()
    
    for coin in coins:
      if coin > curr_total + 1:
        return curr_total + 1
      curr_total+=coin
    return curr_total + 1