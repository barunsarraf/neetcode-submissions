class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                new_s+=c
        return new_s.lower()==new_s[::-1].lower()