def no_teen_sum(a, b, c):
    def fix_teen(n):
        return n if n not in range(13, 20) or n in [15, 16] else 0

    return fix_teen(a) + fix_teen(b) + fix_teen(c)
