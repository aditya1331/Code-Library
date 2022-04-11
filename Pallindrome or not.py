def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1

    return True


if __name__ == '__main__':

    s = 'XYBYBYX'

    if isPalindrome(s):
        print('Palindrome')
    else:
        print('Not Palindrome')