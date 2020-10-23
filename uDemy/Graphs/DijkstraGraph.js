class PriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    this.values.push({val, priority});
    this.values.sort((a,b) => a.priority - b.priority);
  };

  dequeue() {
    return this.values.shift();
  };
}

class WeightedGraph {
  constructor() {
    this.adj = {}
  }

  addVertex(data) {
    if (!this.adj[data]) this.adj[data] = [];
  }

  addEdge(v1, v2, weight) {
    if (this.adj[v1]) this.adj[v1].push({vertex: v2, weight: weight});
    if (this.adj[v2]) this.adj[v2].push({vertex: v1, weight: weight});
  }

  removeEdge(v1, v2) {
    if (this.adj[v1]) this.adj[v1] = this.adj[v1].filter(a => a != v2);
    if (this.adj[v2]) this.adj[v2] = this.adj[v2].filter(a => a != v1);
  }

  removeVertex(data) {
    for (let vertex in this.adj) this.removeEdge(data, vertex);
    delete this.adj[data];
  }

  traverse(v1, v2) {
    let path = [],
        previous = {},
        distances = {},
        queue = new PriorityQueue();
    for (let vertex in this.adj) {
      if (vertex == v1) distances[vertex] = 0;
      else distances[vertex] = Infinity;

      previous[vertex] = null;
      queue.enqueue(vertex, distances[vertex])
    }

    while (queue.values.length) {
      let vertex = queue.dequeue();
      if (vertex.val == v2) {
        while(previous[vertex.val]) {
          path.push(vertex.val);
          vertex.val = previous[vertex.val]
        }
        break;
      }

      for (let neighbor of this.adj[vertex.val]) {
        let distance = distances[vertex.val] + neighbor.weight;
        if (distance < distances[neighbor.vertex]) {
          distances[neighbor.vertex] = distance;
          previous[neighbor.vertex] = vertex.val;
          queue.enqueue(neighbor.vertex, distance);
        }
      }

    }

    return path.concat(v1).reverse();
  }
}

const graph = new WeightedGraph();

graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addVertex('E');
graph.addVertex('F');
graph.addEdge('A','B',4);
graph.addEdge('A','C',2);
graph.addEdge('C','D',2);
graph.addEdge('D','F',1);
graph.addEdge('C','F',4);
graph.addEdge('D','E',3);
graph.addEdge('B','E',3);
graph.addEdge('E','F',1);
console.log(graph.traverse('A', 'E'))
// graph.traverseDFS('Tokyo');
// graph.traverseBFS('Tokyo');
// graph.removeEdge('Tokyo','China');
// graph.removeVertex('China')


// console.log(graph.adj);