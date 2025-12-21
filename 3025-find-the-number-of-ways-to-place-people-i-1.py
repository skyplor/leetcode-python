from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        '''
        We will have a `result` variable and initialise it to 0

        For each pair of points, we need to check for the following:
            - is the first point on the upper left of the second point (can be < or equal)
                - So for 2 points A (x1, y1), B (x2, y2), this rule passes if (x1 <= x2 AND y1 >= y2)
            - are there any other points that lie within (includes on the border) the 2 points
                - We can have a 3rd inner for loop that loops through all remaining points and check if there's intersection
                    - If we encounter any intersection, these 2 points are invalid and we can stop iterating in the 3rd loop
                    - If we are able to finish the iteration, we then add 1 to the result
                    - To determine intersection, new point = (x3, y3)
                        - If x1 == x2 (vertical line): IF x3 == x1 AND y2<=y3<=y1, there's intersection else there's no intersection
                        - If y1 == y2 (horizontal line): IF y3 == y1 AND x1<=x3<=x2, there's intersection else there's no intersection
                        - Else (rectangle): IF x1<=x3<=x2 AND y2<=y3<=y1, there's intersection else there's no intersection

        At the end, we return the result variable

        Time: O(n^3)
        Space: O(1)
        '''

        result = 0
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x1 > x2 or y1 < y2:
                    continue

                intersection = False
                # here, we can safely say that point 1 is on the upper left of point 2
                for x3, y3 in points:
                    if (x3 == x1 and y3 == y1) or (x3 == x2 and y3 == y2):
                        continue

                    # vertical line
                    if x1 == x2:
                        if x1 == x3 and y2 <= y3 <= y1:
                            intersection = True
                            break

                    # horizontal line
                    elif y1 == y2:
                        if y1 == y3 and x1 <= x3 <= x2:
                            intersection = True
                            break

                    else:
                        if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                            intersection = True
                            break

                if not intersection:
                    result += 1

        return result


sol = Solution()
points = [[1, 1], [2, 2], [3, 3]]
print(f'output: {sol.numberOfPairs(points)}, expected: 0')
points = [[6, 2], [4, 4], [2, 6]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')
points = [[3, 1], [1, 3], [1, 1]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')
