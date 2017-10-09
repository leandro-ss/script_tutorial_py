
class Node:
    def __init__(self):
        self.end = False
        self.letters = []
        self.nodes = []
        
##  More ...


class Trie:
    def __init__(self, init=[]):
        self.root = Node()
        for w in init:
            self.insert(w)
    
    def insert(self, word):
        r = self.root
        for let in word:
            try:
                k = r.letters.index(let)
                r = r.nodes[k]
            except ValueError:
                r.letters.append(let)
                n = Node()
                r.nodes.append(n)
                r = n
        ret = not r.end
        r.end = True
        return ret
        
    def search(self, word):
        r = self.root
        for let in word:
            try:
                k = r.letters.index(let)
                r = r.nodes[k]
            except ValueError:
                return False
        return r.end

    def delete(self, word):
        return self.root.delete(word)[0]
        
    def __len__(self):
        return len(self.root)
        
    def num_nodes(self):
        return self.root.num_nodes()
        
    def num_letters(self):
        return self.root.num_letters()


