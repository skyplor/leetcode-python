from typing import List

class Solution:
  def numTeams(self, rating: List[int]) -> int:
    # Solution 1: Errored: TLE - Time Limit Exceeded
    '''
    Using backtracking
    '''
    # res = []
    # def backtracking(cur_team, cur_index):
    #   if len(cur_team) == 3:
    #     res.append(cur_team)
    #     return

    #   if cur_index >= len(rating):
    #     return
      
    #   cur_rating = rating[cur_index]
    #   # if cur_team only has 1 element or if cur_team has 2 elements and cur_value is in the same order, include cur value
    #   if (
    #     (len(cur_team) <= 1)
    #     or (
    #       len(cur_team) == 2
    #       and (
    #         (cur_team[0] < cur_team[1] and cur_team[1] < cur_rating)
    #         or (cur_team[0] > cur_team[1] and cur_team[1] > cur_rating)))):
    #     backtracking(cur_team + [cur_rating], cur_index + 1)
    #   # exclude cur value
    #   backtracking(cur_team, cur_index + 1)

    # backtracking([], 0)
    # return len(res)

    # Solution 2:
    '''
    We use middle soldiers, iterate the rating array,
    check how many ratings on the left of the middle soldier is larger and how many on the right is smaller than middle soldier
    multiply both numbers and add this value to the result
    we don't have to repeat the above to get the opposite since we can calculate the opposite:
      i.e how many on the left of middle soldier is smaller and how many on the right of middle soldier is larger
    At the end, return the result
    '''
    n = len(rating)
    if n < 3:
      return 0

    teams = 0
    for mid in range(n):
      left_smaller = 0
      right_larger = 0

      for left in range(mid):
        if rating[left] < rating[mid]:
          left_smaller += 1

      for right in range(mid + 1, n):
        if rating[right] > rating[mid]:
          right_larger += 1
      teams += left_smaller * right_larger

      left_larger = mid - left_smaller
      right_smaller = n - mid - 1 - right_larger

      teams += left_larger * right_smaller

    return teams

sol = Solution()
rating = [2,5,3,4,1]
# rating = [2,1,3]
# rating = [1,2,3,4]
print(f'output: {sol.numTeams(rating)}')