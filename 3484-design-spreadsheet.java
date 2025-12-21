import java.util.*;

class Spreadsheet {
    Map<String, Integer> cells = new HashMap<>();

    public Spreadsheet(int rows) {

    }

    public void setCell(String cell, int value) {
        this.cells.put(cell, value);
    }

    public void resetCell(String cell) {
        this.cells.remove(cell);
    }

    public int getValue(String formula) {
        String[] sumElements = formula.substring(1).split("\\+");

        int result = 0;
        for (String element : sumElements) {
            if (element.charAt(0) > '9') {
                result += this.cells.getOrDefault(element, 0);
            } else {
                result += Integer.parseInt(element);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
        System.out.println("Output: " + spreadsheet.getValue("=5+7") + ", expected: 12"); // returns 12 (5+7)
        spreadsheet.setCell("A1", 10); // sets A1 to 10
        System.out.println("Output: " + spreadsheet.getValue("=A1+6") + ", expected: 16"); // returns 16 (10+6)
        spreadsheet.setCell("B2", 15); // sets B2 to 15
        System.out.println("Output: " + spreadsheet.getValue("=A1+B2") + ", expected: 25"); // returns 25 (10+15)
        spreadsheet.resetCell("A1"); // resets A1 to 0
        System.out.println("Output: " + spreadsheet.getValue("=A1+B2") + ", expected: 15"); // returns 15 (0+15)
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */