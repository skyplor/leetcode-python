class Solution:
    def maximumEnergy(self, energy: list[int], k: int):
        '''
        We can use prefix sum, and reuse the energy list

        We have a for loop that goes through each magician. At each element, we add the energy gained from energy[i-k] to energy[i], and store it in energy[i]
            - Note that we should only add the energy gained IF it results in a higher energy. If it doesn't, then we are better off just starting from energy[i]
        The end result is the max of the values stored in the energy from energy[n-1-k:n-1]
        '''
        n = len(energy)
        for i in range(k, n):
            current = energy[i]
            energy[i] = energy[i-k] + current if energy[i-k] + current > current else current

        return max(energy[n-k:n])


sol = Solution()
energy = [5, 2, -10, -5, 1]
k = 3
print(f'output: {sol.maximumEnergy(energy, k)}, expected: 3')
energy = [-2, -3, -1]
k = 2
print(f'output: {sol.maximumEnergy(energy, k)}, expected: -1')
energy = [8, -5]
k = 1
print(f'output: {sol.maximumEnergy(energy, k)}, expected: 3')
