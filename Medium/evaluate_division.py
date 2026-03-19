from collections import defaultdict

"""
graph: key -> string, one part of each equation
       value -> dict: key -> string, other part of each equation
                      value -> tuple (solution, inverse or not)

graph[key] -> dict of string: tuple
graph[key][key] -> a tuple (value, inverse indicator)
graph[key][key][index] -> either the value or inverse indicator
"""
# Beat 100% in runtime and 99.73% in memory. Idea is to store all the direct operations and their inverses. When traversing, we need to keep track of where we have been to prevent getting caught in cycles. If we are chaining (['a', 'b'], ['b', 'c'] looking for ['a', 'c']) then we need to perform inverse operation on found value, i.e. multiply.
class Solution:
    def dfs(self, source: str, looking: str, graph: defaultdict(dict), visited: set()) -> float:
        if looking in graph[source]:
            return graph[source][looking][0] ** graph[source][looking][1]
        
        visited.add(source)
        for eqs in graph[source].keys():
            if eqs == source or eqs in visited:
                continue

            val = self.dfs(eqs, looking, graph, visited)
            if val:
                return val * (graph[source][eqs][0] ** graph[source][eqs][1])
        
        return None


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        
        equations_graph = defaultdict(dict)

        for ind, equation in enumerate(equations):
            equations_graph[equation[0]][equation[1]] = (values[ind], 1)
            equations_graph[equation[1]][equation[0]] = (values[ind], -1)
        
        solutions = []

        for query in queries:
            if query[0] not in equations_graph or query[1] not in equations_graph:
                solutions.append(-1.0)
            elif query[0] == query[1]:
                solutions.append(1.0)
            else:
                sol = self.dfs(query[0], query[1], equations_graph, set([query[0]]))
                if sol:
                    solutions.append(sol)
                else:
                    solutions.append(-1.0)
        
        return solutions

            