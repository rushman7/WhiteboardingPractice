def calc_drone_min_energy(route):
  total_min = float('inf')
  reserve = 0
  
  for i in range(1, len(route)):
    if route[i][2] < route[i-1][2]:
      reserve += (route[i-1][2] - route[i][2])
    else:
      reserve -= (route[i][2] - route[i-1][2])
      total_min = min(reserve, total_min)
    
  return abs(total_min) if total_min != float('inf') else 0
