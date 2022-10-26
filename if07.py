def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"
    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0:
        if a % 2 == 0:
            print (a, " positive even number ")
        if a % 2 != 0:
            print (a, " positive odd number ")

    if a < 0:
        if a % 2 == 0:
            print (a, " negative even number ")
        if a % 2 != 0:
            print (a, " negative odd number ")

    if a == 0:
        print("0")
q = (main(0))
    