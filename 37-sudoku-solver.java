import java.util.*;

class Cell {
    int row, col;

    public Cell(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

class SudokuSolverSolution {

    public int getSquareIndex(int row, int col) {
        return 3 * (row / 3) + (col / 3);
    }

    public boolean checkValid(int row, int col, char value, List<Set<Character>> rowSets, List<Set<Character>> colSets,
            List<Set<Character>> squareSets) {
        int squareIdx = getSquareIndex(row, col);
        Set<Character> rowSet = rowSets.get(row);
        Set<Character> colSet = colSets.get(col);
        Set<Character> squareSet = squareSets.get(squareIdx);
        if (rowSet.contains(value) || colSet.contains(value) || squareSet.contains(value)) {
            return false;
        }
        return true;
    }

    public void populate(char[][] board, List<Set<Character>> rowSets, List<Set<Character>> colSets,
            List<Set<Character>> squareSets) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int squareIdx = getSquareIndex(r, c);
                Set<Character> rowSet = rowSets.get(r);
                Set<Character> colSet = colSets.get(c);
                Set<Character> squareSet = squareSets.get(squareIdx);

                char value = board[r][c];
                if (value == '.') {
                    continue;
                }

                rowSet.add(value);
                colSet.add(value);
                squareSet.add(value);
            }
        }
    }

    public void solve(char[][] board, List<Set<Character>> rowSets, List<Set<Character>> colSets,
            List<Set<Character>> squareSets) {
        List<Cell> emptyCells = new ArrayList<>();
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    emptyCells.add(new Cell(r, c));
                }
            }
        }

        backtrack(board, rowSets, colSets, squareSets, emptyCells, 0);
    }

    public boolean backtrack(char[][] board, List<Set<Character>> rowSets, List<Set<Character>> colSets,
            List<Set<Character>> squareSets, List<Cell> emptyCells, int index) {
        if (index == emptyCells.size()) {
            return true;
        }

        Cell cell = emptyCells.get(index);
        for (int i = 1; i < 10; i++) {
            int row = cell.row;
            int col = cell.col;
            char value = (char) (i + '0');
            if (checkValid(row, col, value, rowSets, colSets, squareSets)) {
                board[row][col] = value;
                int squareIdx = getSquareIndex(row, col);
                Set<Character> rowSet = rowSets.get(row);
                Set<Character> colSet = colSets.get(col);
                Set<Character> squareSet = squareSets.get(squareIdx);
                rowSet.add(value);
                colSet.add(value);
                squareSet.add(value);
                if (backtrack(board, rowSets, colSets, squareSets, emptyCells, index + 1)) {
                    return true;
                }

                board[row][col] = '.';
                rowSet.remove(value);
                colSet.remove(value);
                squareSet.remove(value);
            }
        }
        return false;
    }

    public void solveSudoku(char[][] board) {
        List<Set<Character>> rowSets = new ArrayList<>();
        List<Set<Character>> colSets = new ArrayList<>();
        List<Set<Character>> squareSets = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            rowSets.add(new HashSet<>());
            colSets.add(new HashSet<>());
            squareSets.add(new HashSet<>());
        }

        populate(board, rowSets, colSets, squareSets);

        solve(board, rowSets, colSets, squareSets);
    }

    public static void main(String[] args) {
        SudokuSolverSolution sol = new SudokuSolverSolution();
        char[][] board;

        board = new char[][] { { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' }, { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' }, { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' }, { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' }, { '.', '.', '.', '.', '8', '.', '.', '7', '9' } };
        sol.solveSudoku(board);

        System.out.println(String.format(
                "Output: %s, expected: [['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]",
                Arrays.deepToString(board)));
    }
}
