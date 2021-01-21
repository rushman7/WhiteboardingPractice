def minimumWaitingTime(queries):
    if len(queries) <= 1: return 0
    queries.sort()
    total, prev = queries[0], 0
    
    for i in range(1, len(queries)-1):
        prev += queries[i-1]
        total = prev + queries[i] + total
      
    return total