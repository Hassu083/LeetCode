 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Solution:
    def wordBreak(self, s: str, dictionary: List[str]) -> List[str]:
        n = len(s)
        root = self.buildTrie(dictionary)
        
        @cache
        def dp(start, st):
            if start == n:
                ans.append(st[1:]) 
                return
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp(end + 1, st+" "+node.word)
        ans = []
        dp(0, "")
        return ans
    
    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
            node.word = word
        return root