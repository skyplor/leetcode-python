class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        '''
        Since this list of stations is the actual linkage between each city, that means we will know how much power each city can receive using the indices directly
        And because we want to find the maximum possible minimum power,
            - i.e. to calculate power received for all cities, get the one with the smallest,
            - and we want to maximize this number by allocating the additional `k` power stations to the correct city

        To calculate the power received for all cities, we will have store the calculated power in a separate list while traversing through the list of stations
        We can use sliding window technique to add and reduce the number of power stations
        - First, initialise the sliding window by incrementing and calculating the sum and storing the `running_total`
        - Once we reach `r` length, we have the total for index 0. add into `power_available`.
        - Next, we have a for loop that starts from r to len(stations)
        - At each iteration, we do running_total += stations[i] - stations[i - r] and append running_total into power_available
            - e.g. stations=[1, 2, 4, 5, 0], r=1, k=2
            - power_available = [3, 7, 11, 9, 5]
            - currently smallest is 3.
        Next, we will make use of binary search to find the maximum possible minimum.
        Binary search will be from min(power_available) to `sum(stations) + k`
        So we use binary search to find the answer.
        With each iteration, we check if the number is achievable
            - Can I make every city have at least power X with k stations
        '''
        power_available = []
        n = len(stations)
        running_total = 0

        for i in range(r+1):
            if i < n:
                running_total += stations[i]

        power_available.append(running_total)

        for i in range(1, n):
            if i - r - 1 >= 0:
                running_total -= stations[i - r - 1]
            if i + r < n:
                running_total += stations[i + r]
            power_available.append(running_total)

        def is_possible(target):
            x = k
            power_diff = [0] * (n + 1)
            current_add = 0
            for i in range(n):
                current_add += power_diff[i]
                current_power = power_available[i] + current_add

                if current_power < target:
                    need = target - current_power
                    x -= need
                    if x < 0:
                        return False

                    # Place stations at position pos
                    pos = min(i + r, n - 1)

                    # Mark range [pos-r, pos+r] for addition using difference array
                    left = max(0, pos - r)
                    right = min(n - 1, pos + r)
                    power_diff[left] += need
                    if right + 1 <= n:
                        power_diff[right + 1] -= need

                    # Update current_add if this affects current position
                    if left <= i:
                        current_add += need
            return True

        def binary_search(left, right):
            answer = 0
            while left <= right:
                mid = left + (right - left) // 2
                if is_possible(mid):
                    answer = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        left = min(power_available)
        right = sum(stations) + k
        return binary_search(left, right)


sol = Solution()
print(
    f'output: {sol.maxPower(stations=[1, 2, 4, 5, 0], r=1, k=2)}, expected: 5')
print(f'output: {sol.maxPower(stations=[4, 4, 4, 4], r=0, k=3)}, expected: 4')
