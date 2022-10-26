def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    countplus = 0
    countminus = 0

    if a > 0:
        countplus += 1
    if b > 0:
        countplus += 1
    if c > 0:
        countplus += 1
    
    countminus = 3 - countplus 

    if countplus > countminus:
        return countplus
    
    return countminus
