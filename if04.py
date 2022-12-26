def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0:
        number = 1
    if a<0:
        number = 0
    if b>0:
        number = number + 1
    if c>0:
        number = number + 1
    return number
a = 70
b = -45
c = -67
print(main(a, b, c))