class BinTree:
    """ 
    Basic binary search tree implementation. Empty trees denoted
    by None. Assumes values are comparable using '<'. Repeated
    values are accepted.
    """
    def __init__(self, data, left=None, right=None):
        """ 
        Constructor: a node with subtrees
        @param data: node contents
        @param left: left subtree
        @param right: right subtree
        
        """
        self.left = left
        self.right = right
        self.data = data

        
    def insert(self, data):
        """ 
        Inserts a new node with 'data' by searching for the correct
        place in the tree. Chooses right when greater or equal.
        @param data: value to be inserted
        @return: new node
        """
        p = self
        n = BinTree(data)
        while True:
            go_left =  data<p.data
            t = p.left if go_left else p.right
            if not t:
                if go_left:
                    p.left = n
                else:
                    p.right = n
                return n
            p = t

    def draw(self, level=1, indent=3):
        """
        Prints a graphical representation of the tree rotated by 90 degrees.
        
        @param level: node level within the tree
        @param indent: increment between levels
        """
        if self.right:
            self.right.draw(level+1, indent)
            print(level*indent*' ', '/')
        print((level*indent-len(str(self.data)))*' ', self.data)
        if self.left:
            print(level*indent*' ','\\')
            self.left.draw(level+1, indent)
