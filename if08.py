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
    if -10< a//10 <10:
        x = "two-digit"
    if -10< a//100 <10:
        x = "three-digit"
    if a%2==1:
        x = x + " odd number"
    if a%2==0:
        x = x + " even number"
    return x
a =70
print(main(a))