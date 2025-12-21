class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        '''
        We can use binary search for this by searching for the maximum run time.
            - left = 1, right = total of the batteries / n

        At each stage, we check if the mid value is achievable or not.
        To know if it is achievable, we check each battery, get the min(target, cur), sum all these up and if the total is larger than the target * n, that means this is achievable
        But if it is smaller, that means this isn't achievable
        
        Note: for this, we added some optimisation such as early termination in `is_achievable`
        and also updated the binary search to not have to workaround the issue of `left = mid` by tracking the `res` directly
        '''

        def is_achievable(target: int) -> bool:
            total = 0
            required = target * n
            for b in batteries:
                if b < target:
                    total += b
                else:
                    total += target
                
                if total >= required:
                    return True

            return total >= required

        left, right = 1, sum(batteries) // n
        res = 1
        while left <= right:
            mid = left + (right - left) // 2

            if is_achievable(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


sol = Solution()
print(f'output: {sol.maxRunTime(n=2, batteries=[3, 3, 3])}, expected: 4')
print(f'output: {sol.maxRunTime(n=2, batteries=[1, 1, 1, 1])}, expected: 2')
