class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        start = 0 
        end =0
        current_max = 0
        while end<len(s):
            if s[end] in found:
                found.remove(s[start])
                start+=1
            else:
                found.add(s[end])
                current_max = max(end-start+1,current_max)
                end+=1
        return current_max

