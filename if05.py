def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n//10000
    x2=n%10000//1000
    x3=n%10000%1000//100
    x4=n%10000%1000%100//10
    x5=n%10

    if x1>=x2 and x1>=x3 and x1>=x4 and x1>=x5:   
       return x1
    if x2>=x3 and x2>=x4 and x2>=x5 and x2>=x1:
        return x2
    if x3>=x4 and x3>=x5 and x3>=x2 and x3>=x1:
        return x3
    if x4>=x5 and x4>=x1 and x4>=x2 and x4>=x3:
        return x4
    if x5>=x1 and x5>=x2 and x5>=x3 and x5>=x4:
        return x5
print(main(26546))


