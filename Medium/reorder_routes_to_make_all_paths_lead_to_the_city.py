"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

    2 <= n <= 5 * 104
    connections.length == n - 1
    connections[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
"""

"""
I could not get this one on my own. The key insight is that the structure forms a tree, i.e. all the nodes are connected SOMEHOW. We need to determine which edges need to be flipped, and we can therefore add reverse edges to our adjacency list. If we need to use a reverse edge to traverse the tree, we know the source edge is good. If we are using a source edge to traverse the tree, we know this edge needs to be flipped. By indicating source edges with a 1 and reverse edges with a 0, we can simply add the sign to the count which will only increment when we encounter edges that need to be flipped.
"""

from collections import defaultdict
class Solution:
    count = 0

    def dfs(self, node: int, parent: int, adj: defaultdict(List)):
        if node not in adj:
            return
        
        for edge in adj[node]:
            neighbor = edge[0]
            sign = edge[1]
            # This check avoids cycles
            if neighbor != parent:
                self.count += sign
                self.dfs(neighbor, node, adj)
        

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for connection in connections:
            # Add actual edge
            adj[connection[0]].append((connection[1], 1))
            # Add reverse edge with indicator
            adj[connection[1]].append((connection[0], 0))

        self.dfs(0, -1, adj)
        return self.count