""" Exercicio
"""
from stack import Stack
# ...

def parens(arg):
    """Checks for balanced parentheses in a string. 
    @param s: given string; assume no blanks
    @return: True or False
    """
    result = True

    stk = Stack()

    for x in arg:
        stk.push(x)

    try:
        #print ("stk.top:"+str(stk.pop))
        while result and stk.top():
            result = verify_is_closed(stk)

    except IndexError:
        pass

    return result

OPEN_BRACKET = ['(', '{', '[']
CLOSE_BRACKET = [')', '}', ']']

def verify_is_closed (stk, count=0):
    """Checks for balanced parentheses in a string.
    @param s: given string; assume no blanks
    @return: True or False
    """
    result = True
    try:
        compare_actual = stk.pop()

        while stk.top() in CLOSE_BRACKET and result:

            result = verify_is_closed(stk, count+1)

        if result:
            compare_before = stk.pop()

            if (compare_actual == ')' and compare_before != '(') \
            or (compare_actual == ']' and compare_before != '[') \
            or (compare_actual == '}' and compare_before != '{'):
                result = False

    except IndexError:
        result = False
    except Exception:
        raise

    return result

if __name__=="__main__":
    ## Read and print set data
    arg = "[]()[()[]]"
    print(arg)
    print(parens(arg))