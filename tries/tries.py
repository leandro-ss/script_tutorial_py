
class Node:
    def __init__(self):
        self.end = False
        self.letters = []
        self.nodes = []
    

    def num_nodes(self,  count=0, result = 0):

        return self.num_genec()

    def num_letters(self,  count=0, result = 0):
    
        return self.num_genec()-1

    def num_genec(self, result = 0):

        result+=1

        if self.nodes is not None:
            for node in self.nodes:
                result = node.num_genec(result)

        return result


    def __len__(self):
        return self.len_nodes()

    def len_nodes(self,  result=0):

        if self.end:
            result+=1

        if self.nodes is not None:
            for node in self.nodes:
                result = node.len_nodes(result)

        return result


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

    def delete(self, word):
        return self.deleteFromNode( word, self.root)

    def deleteFromNode(self, word, node, posit=0):
        result = True

        #print ("start.node.letters::"+str(node.letters))
        #print ("start::posit="+str(posit))
        #print ("start::word[posit]="+str(word[posit]))

        if posit < len(word):        
            try:

                result = self.deleteFromNode( word, node.nodes[node.letters.index(word[posit])] , posit+1)

            except ValueError:
                #print ("ValueError")
                return False, 0

            #print ("before::len (node.nodes)="+str(len (node.nodes)))
            #print ("before::posit="+str(word[posit]))
            #print ("before.node.letters::"+str(node.letters))
            #print ("result::" +str(result))

        if result:
            #print ("afterif::len (node.nodes)="+str(len (node.nodes)))
            #print ("after::posit="+str(posit))
            #print ("after::word[posit]="+str(word[posit]))
            #print ("after.node.letters::"+str(node.letters))
            #node.letters.remove(word[posit+1])
            node.letters = []
            node.nodes = []
            
            
        return result, posit

        
    def search(self, word):
        r = self.root
        for let in word:
            try:
                k = r.letters.index(let)
                r = r.nodes[k]
            except ValueError:
                return False
        return r.end

    def __len__(self):
        return len(self.root)
        
    def num_nodes(self):
        return self.root.num_nodes()
        
    def num_letters(self):
        return self.root.num_letters()


