def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1 = s[0]
    count =0
    if x1>='0' and x1<='9':
        count+=1
    return count
print(main("12340"))