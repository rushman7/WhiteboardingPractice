class Graph {
  constructor() {
    this.adj = {}
  }

  addVertex(data) {
    this.adj[data] = [];
  }

  addEdge(v1, v2) {
    if (this.adj[v1]) this.adj[v1].push(v2);
    if (this.adj[v2]) this.adj[v2].push(v1);
  }

  removeEdge(v1, v2) {
    if (this.adj[v1]) this.adj[v1] = this.adj[v1].filter(a => a != v2);
    if (this.adj[v2]) this.adj[v2] = this.adj[v2].filter(a => a != v1);
  }
}

const graph = new Graph();

graph.addVertex('Tokyo');
graph.addVertex('London');
graph.addVertex('California');
graph.addVertex('China');
graph.addEdge('Tokyo','China');
graph.addEdge('Tokyo','London');
graph.addEdge('China','California');
graph.removeEdge('Tokyo','China');


console.log(graph);