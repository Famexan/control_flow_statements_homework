def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    x = str(a // 10)
    y = str(a % 10)
    c = int(y+x)

    if c <= a:
        return True

    if c > a:
        return False


q = (main(45))

print(q)
