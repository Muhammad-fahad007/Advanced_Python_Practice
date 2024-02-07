def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    n = len(intervals)
    c = 0
    while (c < n - 1):
        if intervals[c][1] >= intervals[c + 1][0] and intervals[c][1] > intervals[c + 1][1]:
            intervals.pop(c + 1)
            n -= 1
        elif intervals[c][1] >= intervals[c + 1][0]:
            ele = [intervals[c][0], intervals[c + 1][1]]
            intervals.pop(c)
            intervals.pop(c)
            intervals.insert(c, ele)
            n -= 1
            c-=1
        c += 1
    return intervals

x = merge([[1,4],[0,2],[3,5]])
print(x)