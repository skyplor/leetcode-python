from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        We have a list of potential profits based on the job taken.
        For each potential choice, we branch out a decision node. So we can use a 1-D dp for this.
        We sort the jobs by the start time e.g [[1, 3, 50], [2, 4, 10], [3, 5, 40], [3, 6, 70]]
        then we go through each job, we calculate what is the max profit at the index
        dp[i] - i refers to index of the job and dp[i] refers to maximum profit we can get if we start from i.
        At the index, we can either include the job or don't include the job.
            - If we don't include the job, we just go to the next index (i + 1)
            - If we include the job, then we need to do binary search to find the next index that has the start time that is >= the current end time
            - Then we get the max of the 2 i.e dp[i] = max(dp[i+1], dp[j] + current_profit)

        We will do this in reverse order so the dp[i+1] and dp[j] would have been calculated already

        '''
        jobs = []

        def binary_search(left: int, right: int, target: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if target <= jobs[mid][0]:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        n = len(startTime)

        dp = [0] * n
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort(key=lambda x: x[0])

        for i in range(n - 1, -1, -1):
            excl_and_next_job = 0 if i + 1 > n - 1 else dp[i+1]
            _, current_end, current_profit = jobs[i]
            incl_next_job_index = binary_search(i, n - 1, current_end)
            incl_and_next_job = current_profit if incl_next_job_index >= n else current_profit + \
                dp[incl_next_job_index]
            dp[i] = max(incl_and_next_job, excl_and_next_job)

        return dp[0]


sol = Solution()
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
output = sol.jobScheduling(startTime, endTime, profit)
print(f'output: {output}')
