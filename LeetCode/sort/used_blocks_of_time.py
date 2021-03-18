def calendar(times):
    hours = [0] * 24
    # bucket sort
    for start, end in times:
        hours[start] += 1
        hours[end] -= 1
    res, start, total = [], None, 0

    for i, n in enumerate(hours):
        total += n
        if not start and n:
            start= i
        elif start and not total:
            res.append([start, i])
            start = None
    return res