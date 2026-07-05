class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappy = {}
        for i in strs:
            sor = tuple(sorted(i))
            if sor in mappy:
                mappy[sor].append(i)
            else:
                mappy[sor] = [i]
        return list(mappy.values())
        
            
        
            