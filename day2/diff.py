
def diff(obj1, obj2):
    """ Computes a list d1 of elements which are in obj1 but not in obj2, and
    d2 of elements which are in obj2 but not in obj1. Assumes s1 and s2 are
    iterable objects whose elements are not necessarily sorted but 
    which can be compared.  Both lists d1 and d2 should be sorted.
    
    @params1: an iterable  object
    @params2: an iterable  object
    @return: d1, d2 
    """
    i = j = 0
    # Temporary statements in or der to avoid error
    d1 = [] #
    d2 = []
    ###

    obj1 = sorted(obj1)
    obj2 = sorted(obj2)


    try:
        while True:
            if obj1[i] < obj2[j]:

                d1.append(obj1[i])
                i+=1
            elif obj1[i] > obj2[j]:

                d2.append(obj2[j])
                j+=1
            else:

                j+=1
                i+=1

    except IndexError:  ## any error
        d1 += obj1[i:]
        d2 += obj2[j:]

    return d1, d2


if __name__=="__main__":      
    ## Read and print set data
    my1 = [2,5,4,10,12,0]
    my2 = [2,5,4,16,17,1]

    print (diff(my1, my2))