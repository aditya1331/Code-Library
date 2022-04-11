from collections import deque


class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __repr__(self):
        return str((self.begin, self.end))


def mergeIntervals(intervals):

    intervals.sort(key=lambda x: x.begin)

    stack = deque()

    for curr in intervals:

        if not stack or curr.begin > stack[-1].end:
            stack.append(curr)

        if stack[-1].end < curr.end:
            stack[-1].end = curr.end

    while stack:
        print(stack.pop())


if __name__ == '__main__':
    intervals = [Interval(1, 5), Interval(2, 3), Interval(4, 6),
                 Interval(7, 8), Interval(8, 10), Interval(12, 15)]

    mergeIntervals(intervals)