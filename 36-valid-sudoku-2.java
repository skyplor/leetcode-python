import java.util.*;

class ValidSudokuSolution {

    public int getSquareIndex(int row, int col) {
        // rows 0 - 2 and cols 0 - 2 = index 0
        // rows 0 - 2 and cols 3 - 5 = index 1
        // rows 0 - 2 and cols 6 - 8 = index 2
        // rows 3 - 5 and cols 0 - 2 = index 3
        int temp_r = row / 3;
        int temp_c = col / 3;

        return 3 * temp_r + temp_c;
    }

    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rowSets = new ArrayList<>();
        List<Set<Character>> colSets = new ArrayList<>();
        List<Set<Character>> squareSets = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            rowSets.add(new HashSet<>());
            colSets.add(new HashSet<>());
            squareSets.add(new HashSet<>());
        }

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                int squareIdx = getSquareIndex(r, c);
                char value = board[r][c];
                if (value == '.') {
                    continue;
                }
                Set<Character> rowSet = rowSets.get(r);
                Set<Character> colSet = colSets.get(c);
                Set<Character> squareSet = squareSets.get(squareIdx);
                if (rowSet.contains(value) || colSet.contains(value) || squareSet.contains(value)) {
                    return false;
                }
                rowSet.add(value);
                colSet.add(value);
                squareSet.add(value);
            }
        }

        return true;
    }

    public static void main(String[] args) {
        ValidSudokuSolution sol = new ValidSudokuSolution();
        char[][] board;

        board = new char[][] { { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' }, { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' }, { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' }, { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' }, { '.', '.', '.', '.', '8', '.', '.', '7', '9' } };
        System.out.println(String.format("Output: %b, expected: true", sol.isValidSudoku(board)));

        board = new char[][] { { '8', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' }, { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' }, { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' }, { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' }, { '.', '.', '.', '.', '8', '.', '.', '7', '9' } };
        System.out.println(String.format("Output: %b, expected: false", sol.isValidSudoku(board)));
    }
}