def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    str_x = str(x)

    length = len(str_x)
    for i in range(length // 2):
        if str_x[i] != str_x[length - 1 - i]:
            return False

    return True

x = 121
print(isPalindrome(x)) # True

x = 122
print(isPalindrome(x)) # False