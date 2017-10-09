class Stack:
    """ Python list: insert and delete at the end. """
    def __init__(self):
        self.st = []
        
    def push(self, data):
        self.st.append(data)
        
    def pop(self):
        try:
            r = self.st[-1]
            del self.st[-1]
            return r
        except IndexError:
            raise
            
    def top(self):
        try:
            return self.st[-1]
        except IndexError:
            raise
            
    def isempty(self):
        return len(self.st)==0
        
    def __repr__(self):
        return str(self.st)
        
    
        
