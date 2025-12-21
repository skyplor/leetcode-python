from collections import defaultdict


class Spreadsheet:
    '''
    We can either use a hashmap or 2D array
    2D array would be more performant for retrieval as the data is contiguously stored
    hashmap would be easier to implement
    We can go with hashmap first before optimising if need be

    We initialist the hashmap to defaultdict(int) so it defaults to 0 if not set
    '''

    def __init__(self, rows: int):
        self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        # we need to parse the cell to get the column and row (this is necessary only if we expect the cell to be an invalid cell. Otherwise we can just set the key)
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        sum_elements = formula.replace('=', '').split('+')
        result = 0
        for element in sum_elements:
            if element.isdigit():
                result += int(element)
            else:
                result += self.cells[element]

        return result


# Initializes a spreadsheet with 3 rows and 26 columns
spreadsheet = Spreadsheet(3)
# returns 12 (5+7)
print(f'output: {spreadsheet.getValue("=5+7")}, expected: 12')
spreadsheet.setCell("A1", 10)  # sets A1 to 10
# returns 16 (10+6)
print(f'output: {spreadsheet.getValue("=A1+6")}, expected: 16')
spreadsheet.setCell("B2", 15)  # sets B2 to 15
# returns 25 (10+15)
print(f'output: {spreadsheet.getValue("=A1+B2")}, expected: 25')
spreadsheet.resetCell("A1")  # resets A1 to 0
# returns 15 (0+15)
print(f'output: {spreadsheet.getValue("=A1+B2")}, expected: 15')


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
