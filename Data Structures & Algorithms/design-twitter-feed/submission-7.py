class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followage = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.tweets[userId][-10:])
        for f in self.followage[userId]:
            tweets.extend(self.tweets[f][-10:])

        heap = [[-c, t] for c, t in tweets]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(len(heap),10))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followage[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followage[followerId].discard(followeeId)