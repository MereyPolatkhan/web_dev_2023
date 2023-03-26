class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000,
        }

        res = 0

        i = 0

        while (i < len(s)):
            # print(s[i], d[s[i]], res)
            if (i <= len(s) - 2):
                first = d[s[i]]
                second = d[s[i + 1]]

                if (second / first == 10.0 or second / first == 5.0):
                    res += (second - first)
                    i += 2
                else:
                    res += first
                    i += 1

            else:
                res += d[s[i]]
                i += 1
                
        return res
