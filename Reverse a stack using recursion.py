from collections import deque

def insertAtBottom(s, item):

    if not s:
        s.append(item)
        return

    top = s.pop()
    insertAtBottom(s, item)

    s.append(top)


def reverseStack(s):

    if not s:
        return

    item = s.pop()
    reverseStack(s)

    insertAtBottom(s, item)


if __name__ == '__main__':
    s = deque(range(1, 6))
    print('Original stack is', s)
    reverseStack(s)
    print('Reversed stack is', s)
