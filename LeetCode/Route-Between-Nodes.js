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