# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:

# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.


class Twitter:
    def __init__(self):
        self.time = 0 # can't rely on tweet id for recency
        self.followers = defaultdict(set)
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque(maxlen=10)

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers_set = {*self.followers[userId], userId} # should also get their own tweet

        tweet_list = []
        for f in followers_set:
            if f in self.tweets: # if follower has tweeted anything
                tweet_list.extend(list(self.tweets[f]))

        # can also use heap but returning like this for O(nlogn)
        tweet_list.sort(reverse=True)
        return list(map(lambda x: x[1], tweet_list[0:10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)  # 1 followed 2, so 1's feed should include 2nd's

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
