class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS={}
        freqT={}

        for char in s:
            if char in freqS:
                freqS[char]+=1
            else:
                freqS[char]=1

        for charT in t:
            if charT in freqT:
                freqT[charT]+=1
            else:
                freqT[charT]=1

        if(freqS == freqT):
            return True
        else:
            return False
        