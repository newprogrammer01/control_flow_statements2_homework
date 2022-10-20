def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and a<c:
        return a
    if b<c and b<a:
        return b
    if c<a and c<b:
        return c
print(main(-9,0,5))
