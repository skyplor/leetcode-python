from heapq import heappush, heappop
from collections import Counter


class Solution:
    def findXSum(self, nums, k, x):
        '''
        This question is the same as LC 3318.
        The constraints for this question is updated to much larger number of nums.
        So we will need to have a more optimised solution

        We will use a sliding window approach with two pointers to process each query efficiently.

        We maintain 2 heaps with lazy deletion:
        - `top`: min-heap containing the top x elements (smallest/worst of the best at root)
        - `rest`: max-heap containing all other elements (largest/best of the rest at root)

        We also maintain:
        - `frequency`: hashmap tracking current count of each number in the window
        - `top_valid` and `rest_valid`: sets tracking which (count, num) tuples are currently valid in each heap
        - `running_total`: sum of elements in the valid top-x set

        With each iteration of the window:
        1. For the element being removed (at position i - k):
        - Mark its old (count, num) tuple as invalid by removing from the appropriate valid set
        - Update running_total if it was in top_valid
        - Decrement its frequency
        - If new frequency > 0, add the new (count, num) tuple to rest heap and rest_valid set

        2. For the element being added (at position i):
        - Mark its old (count, num) tuple as invalid by removing from the appropriate valid set
        - Update running_total if it was in top_valid
        - Increment its frequency
        - Add the new (count, num) tuple to rest heap and rest_valid set

        3. Call balance() to reorganize the heaps:
        - First, fill top to x elements by promoting from rest (clean stale entries before accessing)
        - Second, remove excess from top if size > x by demoting to rest
        - Third, swap elements between heaps if rest has better elements than top
        - Update running_total whenever elements move in/out of top_valid

        4. Append running_total to results

        Key insight:
        We never actually remove elements from the heaps (O(n) operation).
        Instead, we mark them as invalid in the valid sets (O(1) operation) and clean up stale entries lazily when we access the heap tops (amortized efficient).
        This gives us O(log n) operations throughout.
        '''
        frequency = Counter()
        top = []  # min heap: (count, num) - smallest at top
        rest = []  # max heap: (-count, -num) - largest at top
        top_valid = set()  # tracks valid (count, num) in top
        rest_valid = set()  # tracks valid (count, num) in rest
        running_total = 0
        result = []

        def balance():
            nonlocal running_total

            # Fill top to x elements from rest
            while len(top_valid) < x and rest:
                # Clean stale entries
                while rest and (-rest[0][0], -rest[0][1]) not in rest_valid:
                    heappop(rest)

                if rest:
                    count, num = -rest[0][0], -rest[0][1]
                    heappop(rest)
                    rest_valid.discard((count, num))

                    heappush(top, (count, num))
                    top_valid.add((count, num))
                    running_total += count * num

            # Remove excess from top to rest
            while len(top_valid) > x and top:
                # Clean stale entries
                while top and top[0] not in top_valid:
                    heappop(top)

                if top and len(top_valid) > x:
                    count, num = top[0]
                    heappop(top)
                    top_valid.discard((count, num))

                    heappush(rest, (-count, -num))
                    rest_valid.add((count, num))
                    running_total -= count * num

            # Swap if rest has better elements than top
            while rest and top:
                # Clean stale entries
                while rest and (-rest[0][0], -rest[0][1]) not in rest_valid:
                    heappop(rest)
                while top and top[0] not in top_valid:
                    heappop(top)

                if not rest or not top:
                    break

                rest_elem = (-rest[0][0], -rest[0][1])  # (count, num)
                top_elem = top[0]  # (count, num)

                # Compare: higher count better, or same count but higher num better
                if rest_elem > top_elem:
                    # Swap
                    heappop(rest)
                    rest_valid.discard(rest_elem)
                    heappop(top)
                    top_valid.discard(top_elem)

                    heappush(top, rest_elem)
                    top_valid.add(rest_elem)
                    heappush(rest, (-top_elem[0], -top_elem[1]))
                    rest_valid.add(top_elem)

                    running_total += rest_elem[0] * rest_elem[1]
                    running_total -= top_elem[0] * top_elem[1]
                else:
                    break

        def add(num):
            nonlocal running_total

            # Remove old entry if exists
            old_count = frequency[num]
            if old_count > 0:
                old_elem = (old_count, num)
                # Mark as invalid (lazy deletion)
                if old_elem in top_valid:
                    top_valid.discard(old_elem)
                    running_total -= old_count * num
                elif old_elem in rest_valid:
                    rest_valid.discard(old_elem)

            # Update frequency
            frequency[num] += 1
            new_count = frequency[num]
            new_elem = (new_count, num)

            # Add new entry to rest
            heappush(rest, (-new_count, -num))
            rest_valid.add(new_elem)

            balance()

        def remove(num):
            nonlocal running_total

            # Remove old entry
            old_count = frequency[num]
            old_elem = (old_count, num)

            # Mark as invalid (lazy deletion)
            if old_elem in top_valid:
                top_valid.discard(old_elem)
                running_total -= old_count * num
            elif old_elem in rest_valid:
                rest_valid.discard(old_elem)

            # Update frequency
            frequency[num] -= 1
            new_count = frequency[num]

            if new_count > 0:
                new_elem = (new_count, num)
                heappush(rest, (-new_count, -num))
                rest_valid.add(new_elem)

            balance()

        # Build initial window
        for i in range(k):
            add(nums[i])
        result.append(running_total)

        # Slide window
        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            result.append(running_total)

        return result


sol = Solution()
nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2
print(f'output: {sol.findXSum(nums, k, x)}, expected: [6, 10, 12]')

nums = [3, 8, 7, 8, 7, 5]
k = 2
x = 2
print(f'output: {sol.findXSum(nums, k, x)}, expected: [11, 15, 15, 15, 12]')

nums = [9, 2, 2]
k = 3
x = 3
print(f'output: {sol.findXSum(nums, k, x)}, expected: [13]')
