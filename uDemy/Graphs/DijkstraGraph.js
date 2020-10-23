class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, prio) {
    let node = new Node(val, prio)
    if (!this.values.length) return this.values.push(node);
    this.values.push(node);

    let index = this.values.length-1;
    let parentIndex = Math.floor((index-1)/2);

    while (this.values[index].priority < this.values[parentIndex].priority) {
      [this.values[index], this.values[parentIndex]] = [this.values[parentIndex], this.values[index]]
      index = parentIndex;
      parentIndex = Math.floor((index-1)/2);
      if (index == 0) break;
    }
  }

  dequeue() {
    if (this.values.length < 2) return this.values = [];
    [this.values[0], this.values[this.values.length-1]] = [this.values[this.values.length-1], this.values[0]]
    let max = this.values.pop();
    
    if (this.values.length <= 2) {
      if (this.values.length == 2) {
        if (this.values[0].priority > this.values[1].priority) [this.values[0], this.values[1]] = [this.values[1], this.values[0]]
      }
      return max;
    }

    let curr = 0,
        left = (2*curr) + 1,
        right = (2*curr) + 2

    while (this.values[curr].priority > this.values[left].priority || this.values[curr].priority > this.values[right].priority) {
      if (this.values[left].priority < this.values[right].priority) {
        [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
        curr = left;
        left = (2*curr) + 1;
        right = (2*curr) + 2;
        if (left >= this.values.length) break;
        if (right >= this.values.length) {
          if (this.values[curr].priority > this.values[left].priority) [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
          break;
        }
      } else {
        [this.values[curr], this.values[right]] = [this.values[right], this.values[curr]];
        curr = right;
        left = (2*curr) + 1;
        right = (2*curr) + 2;
        if (left >= this.values.length) break;
        if (right >= this.values.length) {
          if (this.values[curr].priority > this.values[left].priority) [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
          break;
        }
      } 
    }
    
    return max;
  }
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