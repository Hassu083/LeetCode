class TrieNode:
    
    def __init__(self):
        self.chr = {}
        self.wordC = False
        
    def createTrie(self, words):
        root = TrieNode() 
        for word in words:
            rootNode = root
            for chr in word:
                if chr not in rootNode.chr:
                    rootNode.chr[chr] = TrieNode() 
                rootNode = rootNode.chr[chr]
            rootNode.wordC = True
        return root
        
class Solution:
    
    def dfs(self, root, word, n):
        node = root
        for i in range(n):
            if word[i] not in node.chr:
                return word
            node = node.chr[word[i]]
            if node.wordC:
                return word[:i+1]
        return word
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        tree = TrieNode().createTrie(dictionary) 
        for i in range(len(sentence)):
            sentence[i] = self.dfs(tree,sentence[i], len(sentence[i])) 
        return " ".join(sentence) 