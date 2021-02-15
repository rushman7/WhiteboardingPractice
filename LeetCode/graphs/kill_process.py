def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    # g = {}
    # visited = set()
    # ans = []
    
    # for i in range(len(pid)):
    #     if ppid[i] not in g:
    #         g[ppid[i]] = []
    #     g[ppid[i]].append(pid[i])

    # def dfs(v):
    #     ans.append(v)
        
    #     if v in g:
    #         for neighbor in g[v]:
    #             if neighbor not in visited:
    #                 dfs(neighbor)
    
    # dfs(kill)
    # return ans
    q = deque()
    adj_list = defaultdict(list)
    
    for i in range(len(ppid)):
        adj_list[ppid[i]].append(pid[i])
    result = []
    q.appendleft(kill)
    
    while q:
        val = q.pop()
        result.append(val)
        for nei in adj_list[val]:
            q.appendleft(nei)
            
    return result