class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        We can use 2 pointers to loop through each character of each version.
            While we haven't reach the next dot,
                we try to get the integer value by getting the character, casting it to int, incrementing pointer
        '''
        n1, n2 = len(version1), len(version2)
        p1 = p2 = 0
        while p1 < n1 or p2 < n2:
            curr_val_1 = 0
            curr_val_2 = 0
            while p1 < n1 and version1[p1] != '.':
                curr_val_1 = curr_val_1 * 10 + int(version1[p1])
                p1 += 1
            while p2 < n2 and version2[p2] != '.':
                curr_val_2 = curr_val_2 * 10 + int(version2[p2])
                p2 += 1

            if curr_val_1 < curr_val_2:
                return -1
            if curr_val_1 > curr_val_2:
                return 1

            p1 += 1
            p2 += 1

        return 0


sol = Solution()
version1 = "1.2"
version2 = "1.10"
print(f'output: {sol.compareVersion(version1, version2)}, expected: -1')
version1 = "1.01"
version2 = "1.001"
print(f'output: {sol.compareVersion(version1, version2)}, expected: 0')
version1 = "1.0"
version2 = "1.0.0.0"
print(f'output: {sol.compareVersion(version1, version2)}, expected: 0')
