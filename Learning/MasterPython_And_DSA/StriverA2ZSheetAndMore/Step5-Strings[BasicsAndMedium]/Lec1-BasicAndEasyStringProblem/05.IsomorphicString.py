'''

'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        for i in range(len(s)):
            c1,c2 = s[i], t[i]

            if ((c1 in mapS and mapS[c1] != c2) or
            c2 in mapT and mapT[c2] != c1):
                return False
            mapS[c1],mapT[c2] = c2,c1
        return True



# Another solution

'''
Time complexity: O(n)
n is length of input string

Space complexity: O(1)
s and t consist of any valid ascii character.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = i
            if t[i] not in mapT:
                mapT[t[i]] = i
            if mapS[s[i]] != mapT[t[i]]:
                return False
        return True
    

# Another solution 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for sc, tc in zip(s, t):
            if ((sc in map_s_t and map_s_t[sc] != tc) or (
                tc in map_t_s and map_t_s[tc] != sc
            )):
                return False
            map_s_t[sc] = tc
            map_t_s[tc] = sc

        return True