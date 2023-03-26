class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 

        def func(s, t):
            i = 0
            j = 0
            res = ""
            while (i < len(s) and j < len(t)):
                if (s[i] == t[j]):
                    res += s[i]
                    i += 1
                    j += 1
                else:
                    break
            return res


        res = strs[0]

        for i in range(1, len(strs)): 
            fromfunc = func(res, strs[i])
            if (len(fromfunc) == 0):
                return ""
            else:
                res = fromfunc

        return res
            