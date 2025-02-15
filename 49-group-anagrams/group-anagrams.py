from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)  # Dictionary with lists as default values

        for s in strs:
            count = [0] * 26  # Array to store letter counts
            
            for c in s:
                count[ord(c) - ord('a')] += 1  # Count occurrences of each letter
            
            res[tuple(count)].append(s)  # Convert count to tuple and use as key

        return list(res.values())  # Convert to list and return

