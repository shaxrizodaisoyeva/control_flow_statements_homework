def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
        a = a+1
    if a<0:
        a = a-2
    if a==0:
        a = 10
    return a 
a = 0
print(main(a))