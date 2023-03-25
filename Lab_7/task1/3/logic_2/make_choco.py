def make_chocolate(small, big, goal):
    big_bars_needed = goal // 5
    if big_bars_needed > big:
        return -1
    else:
        goal -= big_bars_needed * 5

    if goal > small:
        return -1
    else:
        return goal
