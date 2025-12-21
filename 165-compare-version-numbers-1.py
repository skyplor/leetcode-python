class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        Since each contain only digits, we can split by the dots, get the one with the longer length and loop through the elements.
        In each iteration, we compare both splitted array by casting the string as integer value
        '''
        v1_elements = version1.split('.')
        v2_elements = version2.split('.')
        n1, n2 = len(v1_elements), len(v2_elements)
        for i in range(max(n1, n2)):
            e1 = e2 = 0
            if i < n1:
                e1 = int(v1_elements[i])
            if i < n2:
                e2 = int(v2_elements[i])
                
            if e1 == e2:
                continue
            
            return -1 if e1 < e2 else 1
        
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
