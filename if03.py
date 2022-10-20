def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<=b and b<=c:
        return b
    if b<=c and c<=a:
        return c
    if c<=a and a<=b:
        return a
print(main(0,5,-6))




