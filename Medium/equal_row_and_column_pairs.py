"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 105
"""

# Need to convert the lists to something hashable, so I constructed strings which is probably more expensive than necessary.
from collections import defaultdict

class mySolution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        matches = 0

        for row in grid:
            rows[" ".join([str(a) for a in row])] += 1

        n = len(grid)
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(grid[j][i])
            tmp_word = " ".join([str(a) for a in tmp])
            if tmp_word in rows:
                matches += rows[tmp_word]
        
        return matches

# A more pythonic implimentation of the same solution
class pythonicSolution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        # Keep track of the frequency of each row.
        row_counter = collections.Counter(tuple(row) for row in grid)

        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

            
        return count

# A solution using a prefix tree or trie. The components of the list are a branch of the trie, with a leaf indicating how many times that pattern occured in the rows. When following columns we are then traversing the trie, if no path exists then there is no match. Not any more time or memory efficient in terms of O(n^2) for both, just a different approach.
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a] 
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class trieSolution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)
        
        for row in grid:
            my_trie.insert(row)
        
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)
    
        return count    