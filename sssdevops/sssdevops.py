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
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    return sum(num_lst) / len(num_lst)
