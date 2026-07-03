class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=0
        countt=0
        S=sorted(s)
        T=sorted(t)
        return S==T
       

        