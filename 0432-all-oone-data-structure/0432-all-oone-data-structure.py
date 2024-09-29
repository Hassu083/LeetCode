class Node():
    def __init__(self, level):
        self.level = level
        self.val = set()
        self.p = None
        self.n = None 
        
class Deque:

    def __init__(self):
        self.f = Node(None) 
        self.l = Node(None) 
        self.f.n = self.l
        self.l.p = self.f



def insertAfter(n, val, level):
    node = Node(level)
    node.val = val
    n.n.p = node
    node.n, node.p = n.n, n
    n.n = node
    return node

def delete(node):
    node.p.n, node.n.p = node.n, node.p

    




class AllOne:

    def __init__(self):
        self.deque = Deque()
        self.words = {}
        

    def inc(self, key: str) -> None:
        if key in self.words:
            node = self.words[key]
            node.val.remove(key)
            level = node.level + 1

            if node.n.level == level:
                node.n.val.add(key)
                self.words[key] = node.n
            elif node.n.level == None:
                if not node.val:
                    node.level += 1
                    node.val.add(key)
                else:
                    newNode = insertAfter(node, {key}, level)
                    self.words[key] = newNode
            elif node.n.level > level:
                if not node.val:
                    node.level += 1
                    node.val.add(key)
                else:
                    newNode = insertAfter(node, {key}, level)
                    self.words[key] = newNode

            
            if not node.val:
                delete(node)

        else:
            level = 1

            if self.deque.f.n.level != 1:
                node = insertAfter(self.deque.f, set(), 1)
            else:
                node = self.deque.f.n
            self.words[key] = node
            node.val.add(key)
            

        

    def dec(self, key: str) -> None:
        node = self.words[key]
        node.val.remove(key)
        level = node.level - 1

        if level == 0:
            del(self.words[key])
            if not node.val:
                delete(node)
            return 

        if node.p.level == level:
            node.p.val.add(key)
            self.words[key] = node.p
        elif node.p.level == None:
            if not node.val:
                node.level -= 1
                node.val.add(key)
            else:
                newNode = insertAfter(node.p, {key}, level)
                self.words[key] = newNode
        elif node.p.level < level:
            if not node.val:
                node.level -= 1
                node.val.add(key)
            else:
                newNode = insertAfter(node.p, {key}, level)
                self.words[key] = newNode

        
        if not node.val:
            delete(node)
       
        

    def getMaxKey(self) -> str:
        # node = self.deque.f
        # while node:
        #     print(node.val, node.level)
        #     node = node.n
        # print()
        for val in self.deque.l.p.val:
            return val
        return ''
        

    def getMinKey(self) -> str:
        # node = self.deque.f
        # while node:
        #     print(node.val, node.level)
        #     node = node.n
        # print()
        for val in self.deque.f.n.val:
            return val
        return ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()