function isConnectedBFS(graph, s, t) {
  let v = new Set(),
    q = [s];

  while (q.length > 0) {
    let node = q.shift();
    for (let n of graph[node]) {
      if (!v.has(n)) {
        if (n === t) {
          return true;
        }
        v.add(n);
        q.push(n);
      }
    }
  }

  return false;
}


function isConnectedDFS(graph, s, t) {
  return dfs(graph, new Set(), s, t)
}

function dfs(graph, v, s, t) {
  if (s === t) return true;
  v.add(s);
  for (n of graph[s]) {
    if (!v.has(n)) {
      if (dfs(graph, v, n, t)) {
        return true
      }
    }
  }
  return false
}