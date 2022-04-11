# Function to find the lexicographically minimal string rotation
def findLexicalMinRotation(s):
    # to store the lexicographic minimum string
    min = s

    for _ in range(len(s)):

        # left-rotate the string by 1 unit
        s = s[1:] + s[0]

        # update the result if the rotation is minimum so far
        if s < min:
            min = s

    return min


if __name__ == '__main__':
    s = 'bbaaccaadd'
    print("The lexicographically minimal rotation of s is",
          findLexicalMinRotation(s))