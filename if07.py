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
    if a>0:
        x = "positive"
    if a<0:
        x = "negative"
    if a==0:
        x = "the number is zero"
    if a%2==1:
        x = x + " odd number"
    if a%2==0:
        if a!=0:
            x = x + " even number"
    return x
a = 0
print(main(a))