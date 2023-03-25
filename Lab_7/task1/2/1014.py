class Solution:    
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        a = [int(-1e9)] * len(values)
        b = [int(-1e9)] * len(values)

        for i in range(len(values)):
            if (i != len(values) - 1):
                a[i] = values[i] + i 
            if (i != 0):
                b[i] = values[i] - i 

        

        for i in range(1, len(a) - 1):
            a[i] = max(a[i], a[i - 1])

        for i in range(len(b) - 2, 0, -1):
            a[i] = max(a[i], a[i + 1])

        res = int(-1e9)

        for i in range(0, len(a) - 1):
            res = max(res, a[i] + b[i + 1])

        return res


