def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a<0:
        number = 1
    if a>0:
        number = 0
    if b<0:
        number = number + 1
    if c<0:
        number = number + 1
    return number
a = 67
b = -90
c = -87
print(main(a, b, c))