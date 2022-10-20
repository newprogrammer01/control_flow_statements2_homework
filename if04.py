def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
       return 0
    if a>b:
        return a
    if b>a:
        return b
print(main(-3,0))
