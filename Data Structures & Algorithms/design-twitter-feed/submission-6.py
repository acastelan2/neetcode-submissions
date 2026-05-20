class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.tweetMap[userId][-10:])
        for f in self.followMap[userId]:
            tweets.extend(self.tweetMap[f][-10:])

        heap = [[-c, t] for c, t in tweets]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(len(heap),10))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)