class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        i=len(shifts)-2
        while i>-1:
            shifts[i]+=shifts[i+1]
            i-=1
        res=list(s)
        i=0
        while i<len(s):
            res[i] = chr((ord(s[i])-ord('a')+shifts[i])%26 + ord('a'))
            i+=1
        return ''.join(res)
