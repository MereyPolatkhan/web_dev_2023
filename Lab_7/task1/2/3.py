class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {} 
        cur_len = 0 
        start = 0
        maximum = 0
      
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= start:
                start = sub[letter] + 1
                cur_len = i - sub[letter] 
                sub[letter] = i

            else:
                sub[letter] = i
                cur_len += 1
                if maximum < cur_len:
                    maximum = cur_len

        return maximum

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set() 
            
        start = 0
        res = 0
        
        for i in range(len(s)):
            while (s[i] in st):
                st.remove(s[start])
                start += 1
            
            st.add(s[i])
            res = max(res, i - start + 1)
        
        return res
        
            