
def counts(t, count_negative=0, count_neutral=0, count_positive=0, ite=0):
    """ counts
    """
    if t is not None:

        if t.data > 0:
            count_positive += 1
        elif t.data < 0:
            count_negative += 1
        elif t.data == 0:
            count_neutral += 1
        else:
            count_neutral += 1

        #print("count_positive::"+str(count_positive))
        #print("count_negative::"+str(count_negative))
        #print("count_neutral::"+str(count_neutral))
        #print("data::"+str(t.data))
        #print("ite::"+str(ite))

        # Temporary results
        if t.left is not None:
            #print("::left::")
            count_negative, count_neutral, count_positive = counts(t.left, count_negative, count_neutral, count_positive, ite+1)

        if t.right is not None:
            #print("::right::")
            count_negative, count_neutral, count_positive = counts(t.right, count_negative, count_neutral, count_positive, ite+1)

    return  count_negative, count_neutral, count_positive
