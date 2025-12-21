class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        '''
        We can use binary search for this by searching for the maximum run time.
            - left = 1, right = total of the batteries / n

        At each stage, we check if the mid value is achievable or not.
        To know if it is achievable, we check each battery, get the min(target, cur), sum all these up and if the total is larger than the target * n, that means this is achievable
        But if it is smaller, that means this isn't achievable
        
        Note: for the binary search, since we are using `left = mid`, we need to round mid up to prevent unlimited looping.
            - So during calculation, instead of `mid = left + (right - left) // 2`, use `mid = left + (right - left + 1) // 2` instead
            
            If we are using `right = mid`, we need to round mid down so `mid = left + (right - left) // 2` is fine
        '''

        def is_achievable(target: int) -> bool:
            total = 0
            for b in batteries:
                total += min(b, target)

            return total >= target * n

        left, right = 1, sum(batteries) // n
        while left < right:
            mid = left + (right - left + 1) // 2

            if is_achievable(mid):
                left = mid
            else:
                right = mid - 1

        return left


sol = Solution()
print(f'output: {sol.maxRunTime(n=2, batteries=[3, 3, 3])}, expected: 4')
print(f'output: {sol.maxRunTime(n=2, batteries=[1, 1, 1, 1])}, expected: 2')
