"""
Main python file for the sssdevops example
"""

# import statements go there

def mean(num_lst):
    """
    This function calculates the average of a list of numbers

    Parameters
    -------------
    num_lst : list
    List of numbers to calculate the average of

    Returns
    -------------
    The average/mean of num_lst

    Examples
    --------------
    >>> mean([1,2,3,4,5])
    3.0
    """

    total = 0
    for i in num_lst:
        total += i
    num = len(num_lst)
    return total/num
