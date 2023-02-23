def merge(intervals):
    # My Solution
    # i = 0
    # intervals.sort()
    # while i < len(intervals) - 1:
    #     merge_intervals = []
        
    #     if intervals[i+1][0] <= intervals[i][1]:
    #         merge_intervals.append(intervals[i][0])
    #         merge_intervals.append(max(intervals[i][1], intervals[i+1][1]))
    #         intervals = intervals[:i] + intervals[i+2:] 
    #         intervals.insert(i, merge_intervals)
    #     else:
    #         i += 1
    # return intervals

    res = []
    for interval in sorted(intervals):
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

    return res

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))