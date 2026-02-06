class mySolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        
        for ind, char in enumerate(word1):
            s = s + char
            if ind < len(word2):
                s = s + word2[ind]

        if len(word1) < len(word2):
            s = s + word2[len(word1):]
        
        return s

# Essentially the same solution, mine is actually faster with the same memory used
class optimalSolution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)