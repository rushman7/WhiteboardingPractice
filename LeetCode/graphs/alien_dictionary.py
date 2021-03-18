class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = Counter({c:0 for word in words for c in word})
        result = ''
        
        for word1, word2 in zip(words, words[1:]):
            for prev, curr in zip(word1, word2):
                if curr != prev:
                    if curr not in graph[prev]:
                        graph[prev].add(curr)
                        indegree[curr]+=1
                    break
            else:
                if len(word2) < len(word1): return ""
                    
        queue = deque([v for v in indegree if indegree[v] == 0])
        
        while queue:
            vertex = queue.popleft()
            result+= vertex
            for nei in graph[vertex]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
                
        return result if len(result) == len(indegree) else ""