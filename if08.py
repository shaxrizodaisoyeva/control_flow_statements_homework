def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    x = ""
    if a>9 and a<100:
        x = "two-digit"
    if a>99 and a<1000:
        x = "three-digit"
    if a%2==1:
        x = x + " odd number"
    if a%2==0:
        x = x + " even number"
    return x
a =7000
print(main(a))