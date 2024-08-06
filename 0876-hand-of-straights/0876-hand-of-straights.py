# TC: O(nlogn) + O(n)
# SC: O(n)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        hand.sort()
        
        hashMap = defaultdict(int)

        for i in range(len(hand)):
            hashMap[hand[i]] += 1

        while hashMap:

            start = next(iter(hashMap))
            for i in range(start, start + groupSize):

                if i not in hashMap:
                    return False

                hashMap[i] -= 1
                if hashMap[i] == 0:
                    del hashMap[i]

        return True






        

        

          