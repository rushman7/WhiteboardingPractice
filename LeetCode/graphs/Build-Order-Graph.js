function findBuildOrder(projects, dependencies) {
  let adj = {};
  let result = [];
  let visited = new Set();
  let path = new Set();

  projects.forEach(project => adj[project] = []);
  dependencies.forEach(edge => adj[edge[1]].push(edge[0]));
  projects.forEach(project => sort(adj, visited, result, path, project));
  
  return result
}

function sort(adj, visited, result, path, project) {
  if (visited.has(project)) return;

  visited.add(project);
  path.add(project);
  for (n of adj[project]) {
    sort(adj, visited, result, path, n)
  }
  path.delete(project);
  result.push(project)
}