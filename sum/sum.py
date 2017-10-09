""" Exercicio
"""
# ...

def sum(args):
    """Checks for balanced parentheses in a string. 
    @param s: given string; assume no blanks
    @return: True or False
    """        

    return verify_is_number(args)

def verify_is_number (args, before=''):
    """Checks for balanced parentheses in a string.
    @param s: given string; assume no blanks
    @return: True or False
    """
    #print ("1+before::"+str(before))
    result = 0

    if isinstance( args, int):

        result=args
    else: 
        for a in args:

            if isinstance(a, int):
                result +=a
            else:
                result += verify_is_number(a)

    return result

if __name__=="__main__":      
    ## Read and print set data
    my = eval('[[[6,5],4,[3,2,1]],0]')
    print (my)
    print(sum(my))



    