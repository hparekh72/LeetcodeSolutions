class Twitter:

    def __init__(self):
        self.count = 0 # Time
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId


    def postTweet(self, userId: int, tweetId: int) -> None: # TC: O(1), SC: O(1)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


    # This function has a similar intuition to the "Merge k Sorted Lists Problem"
    def getNewsFeed(self, userId: int) -> List[int]:  
        # TC: O(10 * k), where k is the number of users the given user follows.
        # It takes O(k) to iterate over the followed users and O(10 * logk) to manege the heap operations for upto 10 tweets
        # SC: O(k) for the heap, where k is the number of followed users.

        res = [] # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId) # Follow themself 
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
            
        heapq.heapify(minHeap) 

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None: # TC: O(1), SC: O(1)
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None: # TC: O(1), SC: O(1)
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)