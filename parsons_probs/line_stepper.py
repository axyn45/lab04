def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"
    if abs(start%2)!=k%2 or k<abs(start):
        return 0

    def recurr(pos,steps_remain):
        if pos==0 and steps_remain==0: return 1
        if steps_remain==0: return 0
        
        return recurr(pos-1,steps_remain-1)+recurr(pos+1,steps_remain-1)
            

    return recurr(start-1,k-1)+recurr(start+1,k-1)

# print(line_stepper(0,2))