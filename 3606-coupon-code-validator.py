class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        '''
        We create 4 lists, one for each business line, containing the valid codes for each business line
        Next, we go through each code, check if code is valid and is active.
            - if so, we append the code to the list for the business line
            
        At the end, we return a list of sorted codes for each business line
        '''
        electronics, grocery, pharmacy, restaurant = [], [], [], []
        for i, c in enumerate(code):
            if not c or not c.replace('_', 'a').isalnum() or not isActive[i]:
                continue
            business = businessLine[i]
            if business == 'electronics':
                electronics.append(c)
            elif business == 'grocery':
                grocery.append(c)
            elif business == 'pharmacy':
                pharmacy.append(c)
            elif business == 'restaurant':
                restaurant.append(c)
        
        return sorted(electronics) + sorted(grocery) + sorted(pharmacy) + sorted(restaurant)
        
sol = Solution()
print(f'output: {sol.validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True])}, expected: ["PHARMA5","SAVE20"]')
print(f'output: {sol.validateCoupons(code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [False,True,True])}, expected: ["ELECTRONICS_50"]')