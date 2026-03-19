"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""
# Little convoluted, but we are treating the isConnected as a graph with the index acting as a node and the corresponding list as the edge list. Set of visited nodes, go through isConnected indices and if not already visited gather unvisited neighbors. Follow all neighbors and add their direct neighbors that have not been visited etc. etc. Should be n^2 time and n space
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited_nodes = set()
        neighborhoods = 0

        for ind, edge_list in enumerate(isConnected):
            if ind in visited_nodes:
                continue
            
            # There is a new neighborhood, and we have visited a node
            neighborhoods += 1
            visited_nodes.add(ind)

            # Get direct neighbors of the given node that haven't been visited yet
            new_neighbors = set([ind for ind, edge_flag in enumerate(edge_list) if edge_flag == 1 and ind not in visited_nodes])
            while new_neighbors:
                neighbor = new_neighbors.pop()
                if neighbor in visited_nodes:
                    continue
                visited_nodes.add(neighbor)
                new_neighbors.update([ind for ind, edge_flag in enumerate(isConnected[neighbor]) if edge_flag == 1 and ind not in visited_nodes])
        
        return neighborhoods

# dfs solution, simpler and faster but same complexity stop being afraid of recursion
class dfsSolution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size

        for i in range(size):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents

class bfsSolution:
    def bfs(self, node, isConnected, visited):
        from collections import deque

        queue = deque([node])
        visited[node] = True

        while queue:
            node = queue.popleft()

            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                numberOfComponents += 1
                self.bfs(i, isConnected, visited)

        return numberOfComponents
            
           

            
        