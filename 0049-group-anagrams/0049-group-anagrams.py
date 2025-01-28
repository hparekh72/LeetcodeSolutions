class Solution:



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m -> no. of string
        # n -> len of longest string

        # TC: O(m * nlogn)
        # SC: (m * n)
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m -> no. of string
        # n -> len of longest string

        # TC: O(m * n)
        # SC: (m * n)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())
        
        