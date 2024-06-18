from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Twitter:

    def __init__(self):
      self.interval = 0
      self.followerMap = defaultdict(set)
      self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.tweetMap[userId].append([self.interval, tweetId])
      self.interval -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
      # get 10 most recent tweetIds
      self.followerMap[userId].add(userId)
      res = []
      mostRecentHeap = []
      for followeeId in self.followerMap[userId]:
        if followeeId in self.tweetMap:
          index = len(self.tweetMap[followeeId]) - 1
          interval, tweetId = self.tweetMap[followeeId][index]
          heappush(mostRecentHeap, [interval, tweetId, followeeId, index - 1])
      
      while mostRecentHeap and len(res) < 10:
        interval, tweetId, followeeId, index = heappop(mostRecentHeap)
        res.append(tweetId)
        if index >= 0:
          nextInterval, nextTweetId = self.tweetMap[followeeId][index]
          heappush(mostRecentHeap, [nextInterval, nextTweetId, followeeId, index - 1])
          
      return res

    def follow(self, followerId: int, followeeId: int) -> None:
      self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
      self.followerMap[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
