Given an array of strings arr[] representing an infix expression, we have to evaluate it. An infix expression is of the form "operand1 operator operand2" (e.g., "a + b"), where the operator is written between the two operands.

**Note:** Infix expressions follow precedence: ^ (highest, right-to-left), then \* and /, and finally + and - (left-to-right). Division / uses **floor division**.

**Examples:**

```
Input: arr[] = ["100", "+", "200", "/", "2", "*", "5", "+", "7"]
Output: 607

Explanation:
  The expression can be directly read as: (100 + 200 / 2 * 5 + 7).

  Now, evaluate step by step:
    200 / 2 = 100
    100 * 5 = 500
    500 + 100 = 600
    600 + 7 = 607
  Final Answer: 607


Input: arr[] = ["2", "^", "3", "^", "2"]
Output: 512
Explanation: ^ is right-associative → 2 ^ (3 ^ 2) = 2 ^ 9 = 512.
Final Answer: 512
```