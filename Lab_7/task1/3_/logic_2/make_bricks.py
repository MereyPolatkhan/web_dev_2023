def make_bricks(small, big, goal):
    max_big_bricks = goal // 5 if goal >= 5 else big if goal <= big * 5 else 0
    
    remaining_length = goal - max_big_bricks * 5
    
    return small >= remaining_length
