class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram - s and t (all character) is made up of the same characters
        # Solution - count occurnece of each character in a string 
        # Two Hashmaps (with character as key and count being key value)
        # If we make sure both strings are the same length, then we only need to
        # iterate through one hashmap and compare it to the other. 

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True
