class Solution:
    def isValid(self, s: str) -> bool:
        d = {']':'[','}':'{',')':'('}
        stack = []
        for i in range(len(s)):
            if s[i] in ('{','(','['):
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]==d[s[i]]:
                        stack.pop()
                    else:
                        return False
        print(stack)
        return len(stack)==0
