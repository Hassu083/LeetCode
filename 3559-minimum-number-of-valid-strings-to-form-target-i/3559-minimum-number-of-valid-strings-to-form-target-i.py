class TrieNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_word = False  

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  
     
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie = trie.root
        
        n = len(target)
        pq = [(0, 0)]  # (steps, index in target)
        distances = [float('inf')] * (n + 1)
        distances[0] = 0  
        
        
        while pq:
            steps, i = heapq.heappop(pq)

            
            if steps > distances[i]:
                continue
            
            node = trie
            for j in range(i, n):
                if target[j] not in node.children:
                    break
                node = node.children[target[j]]
                
                if distances[j + 1] > steps + 1:
                    distances[j + 1] = steps + 1
                    heapq.heappush(pq, (steps + 1, j + 1))
        # print(distances)
        return distances[n] if distances[n] != float('inf') else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        