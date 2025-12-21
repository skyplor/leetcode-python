from itertools import permutations, combinations
from bisect import bisect_right

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        '''
        We will first generate a list of beautiful numbers. It should be a small list. After that we just go through each number and return the first number greater than n
        '''
        def gen_beautiful_numbers() -> list[int]:
            bases = [str(i) * i for i in range(1, 7)]

            beautiful_numbers = set()
            limit = 10**7

            for size in range(1, len(bases) + 1):
                for combo in combinations(bases, size):
                    combined = ''.join(combo)
                    if len(combined) > 7:
                        continue
                    for p in set(permutations(combined)):
                        temp = int("".join(p))
                        if temp < limit:
                            beautiful_numbers.add(temp)

            for base in bases:
                beautiful_numbers.add(int(base))

            return sorted(beautiful_numbers)
            
        numbers = gen_beautiful_numbers()
        idx = bisect_right(numbers, n)
        return numbers[idx]


sol = Solution()
print(f'output: {sol.nextBeautifulNumber(1)}, expected: 22')
print(f'output: {sol.nextBeautifulNumber(1000)}, expected: 1333')
print(f'output: {sol.nextBeautifulNumber(3000)}, expected: 3133')
print(f'output: {sol.nextBeautifulNumber(59866)}, expected: 122333')
print(f'output: {sol.nextBeautifulNumber(748601)}, expected: 1224444')
