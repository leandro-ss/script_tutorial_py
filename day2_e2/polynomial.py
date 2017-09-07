from copy import deepcopy as dcp

class Polynomial:
    """Implements polynomials in one variable as a Python list of terms
    in decreasing order of exponents. Each term is a pair [ exponent,
    coefficient ]. Only non-null terms are included.
    """
    def __init__(self, ini=[]):
        """ Constructor. Optional argument is an arbitrary object
        which allows iteration yielding terms to initialize the
        polynomial. It is assumed that the terms are already ordered.
        """
        self.terms = [ t for t in ini ]
        
    def __repr__(self):
        """  Builds the representation of an instance. 
        """
        terms = self.terms
        rep = ""
        if not terms:
            return "0"
        for t in terms:
            if t[0]: # >0
                rep += ("%+dx^%d" % (t[1],t[0]))
            else:
                rep += ("%+d " % t[1])
        return rep[:-1]  ## remove last space

        
    def new_term(self, term):
        """ Inserts a term into the polynomial. In case a term with
        the same exponent already exists, it is replaced. It assumes
        that the terms of the polynomial are ordered.
        @param term: the term (pair) to be inserted
        """
        pass  ## Avoids compilation error 
        
        ###  TO BE COMPLETED ###
                
    def add_poly(self, other):
        """ Implements addition of two polynomials. Function deepcopy is
        used, whenever necessary, in order to avoid term sharing.
        @param other: polynomial to be added
        @return: sum of the two polynomials
        
        """
        return []  ## Avoids compilation error 
        
        ###  TO BE COMPLETED ###
         
        
## There should be more methods!


                
                

if __name__=="__main__":
    ## Read and print set data
    
    print(arg)
    print(parens(arg))

