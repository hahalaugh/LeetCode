class Solution(object):
    def reverseOnlyLetters(self, S):
        #利用栈
        stack = []
        s = list(S)
        for c in s:
            if c.isalpha():stack.append(c)
        
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = stack.pop()
        
        return "".join(s)
        
    def reverseOnlyLettersTwoPointer(self, S):
        #利用Two Pointer
        s = list(S)
        i, j = 0, len(s)-1

        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        
        return "".join(s)
                