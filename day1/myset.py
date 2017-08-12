""" This unnecessary class implements sets using lists."""
class MySet:
    """ This unnecessary class implements sets using lists.
    """
    def __init__(self, element=None):
        """ constructor. """
        self.myset = list()  # empty set
        self.union(element)

    def __repr__(self):
        """ toString """
        self.myset.sort()
        return "{%s}" % str(self.myset)[1:-1]

    def __eq__(self, elements):
        """ equals
        @param: elements
        @return: self.myset == elements
        """
        return self.myset == elements

    def __len__(self):
        """ lenght
        @return: size of the set
        """
        return len(self.myset)

    def __iter__(self):
        """ Iterator 
        @return: a iterator over myset
        """
        for element in self.myset:
            yield element

    def __contains__(self, element):
        """ Contains
        @param
        @return
        """
        if element in self.myset:
            return True
        return False

    def add(self, element):
        """ Adds a new element to the set.

        @param element: value to be added
        @return: True if it is a new element, False otherwise
        """
        if element in self.myset:
            return False
        self.myset.append(element)
        return True

    def remove(self, element):
        """ Removes an element from the set.
        @param element: value to be removed
        @return: True if it was in the set, False otherwise
        """
        ms = self.myset
        try:
            k = ms.index(element)
        except ValueError:
            return False
        del ms[k]
        return True

    def union(self, element):
        """ Add collections
        @param:element to union
        """
        if isinstance(element, list):
            for el in element:
                if el not in self.myset:
                    self.myset.append(el)
        if isinstance(element, int):
            if element  not in self.myset:
                self.myset.append(element)

        return self.myset

    def intersection(self, elements):
        """ Intersection collections
        @param:elements with compare
        @return:a list with elements in common
        """
        result = []
        for el in elements:
            if el in self.myset:
                result.append(el)

        return "{%s}" % str(result)[1:-1]

    def difference(self, elements):
        """ Intersection collections
        @param:elements with compare
        @return:a list with elements in common
        """
        result = []
        for el in self.myset:
            if el not in elements:
                result.append(el)
        
        result.sort()
        return "{%s}" % str(result)[1:-1]

    def issubset(self, elements):
        """ Intersection collections
        @param:elements with compare
        @return:a list with elements in common
        """
        result = True
        for el in self.myset:
            if el not in elements:
                result = False

        return result

    def issuperset(self, elements):
        """ Intersection collections
        @param:elements with compare
        @return:a list with elements in common
        """
        result = True
        for el in elements:
            if el not in self.myset:
                result = False

        return result


if __name__=="__main__":      
    ## Read and print set data
    my = MySet()

    my.union([2, 5, 4, 10, 12])
    print(my)

    my.union([3, 4, 5, 6, 10])
    print(my)
