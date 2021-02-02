def validStartingCity(distances, fuel, mpg):
    curr_gas = 0
    min_gas = 0
    res = 0
    
    for i in range(len(distances)):
      next_gas = fuel[i] * mpg
      curr_gas = next_gas + curr_gas - distances[i]
      if curr_gas < min_gas:
        res = i+1
        min_gas = curr_gas
    
    return res % len(distances)
