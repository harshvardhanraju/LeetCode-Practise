class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            # count = [0] * 26  # Assuming lowercase English letters
            # for char in word:
            #     count[ord(char) - ord('a')] += 1
            # key = tuple(count)
     
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        return list(anagrams.values())