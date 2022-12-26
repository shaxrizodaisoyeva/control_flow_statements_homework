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
    if a>0:
        number = 1
    if a<0:
        number = 0
    if b>0:
        number = number + 1
    if c>0:
        number = number + 1
    return number
a = -57
b = 98
c = 45
negative = 3 - main(a, b, c)
print("There are",main(a, b, c), "positive numbers")
print("There are", negative, "negative numbers")