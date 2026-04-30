class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            if(set(s) == set(t)):
                count_s = {}
                count_t = {}

                for char in s:
                    count_s[char] = s.count(char)
                    count_t[char] = t.count(char)
            
                if(count_s == count_t):
                    return True
            
        
        return False
            