# Julius Baer Codility Task Variations

## 🎯 Overview
Based on the cheat sheet patterns, here are ALL possible variations you might encounter. Practice each one to be fully prepared.

---

# 📝 TASK A VARIATIONS (String/Array Manipulation)

## **A1: Sort Digits Descending** ⭐ MOST LIKELY
**Problem:** Extract all individual digits and sort them in descending order.

**Examples:**
```
Input: "1,2,34"        Output: "4321"
Input: "1||2,,,,3"     Output: "321"
Input: "-1,2,3"        Output: "321"
```

**Method Signature:**
```java
public String sortDigitsDesc(String input) { }
```

---

## **A2: Sort Digits Ascending**
**Problem:** Extract all individual digits and sort them in ascending order.

**Examples:**
```
Input: "1,2,34"        Output: "1234"
Input: "3||1,,,,2"     Output: "123"
Input: "-3,1,2"        Output: "123"
```

**Method Signature:**
```java
public String sortDigitsAsc(String input) { }
```

---

## **A3: Sort Numbers Descending**
**Problem:** Extract whole numbers and sort them in descending order, return as array or comma-separated string.

**Examples:**
```
Input: "1,2,34"        Output: [34, 2, 1] or "34,2,1"
Input: "10||2,,,,30"   Output: [30, 10, 2] or "30,10,2"
Input: "-1,2,34"       Output: [34, 2, 1] or "34,2,1"
```

**Method Signature:**
```java
public int[] sortNumbersDesc(String input) { }
// OR
public String sortNumbersDescStr(String input) { }
```

---

## **A4: Sort Numbers Ascending**
**Problem:** Extract whole numbers and sort them in ascending order.

**Examples:**
```
Input: "34,1,2"        Output: [1, 2, 34] or "1,2,34"
Input: "30||10,,,,2"   Output: [2, 10, 30] or "2,10,30"
```

**Method Signature:**
```java
public int[] sortNumbersAsc(String input) { }
```

---

## **A5: Reverse Token Order**
**Problem:** Reverse the order of extracted tokens (numbers or digits).

**Examples:**
```
Input: "1,2,34"        Output: "34,2,1"
Input: "1||2,,,,3"     Output: "3,2,1"
Input: "10,20,30"      Output: "30,20,10"
```

**Method Signature:**
```java
public String reverseTokens(String input) { }
```

---

## **A6: Reverse Entire String**
**Problem:** Reverse the string character by character (ignoring delimiters in final result).

**Examples:**
```
Input: "1,2,34"        Output: "4321"
Input: "abc,def"       Output: "fedcba"
```

**Method Signature:**
```java
public String reverseString(String input) { }
```

---

## **A7: Get Largest/Smallest Number**
**Problem:** Find the largest or smallest number in the input.

**Examples:**
```
Input: "1,2,34"        Largest: 34, Smallest: 1
Input: "100||2,,,,3"   Largest: 100, Smallest: 2
```

**Method Signature:**
```java
public int findLargest(String input) { }
public int findSmallest(String input) { }
```

---

## **A8: Extract Unique Elements**
**Problem:** Extract unique digits or numbers, remove duplicates.

**Examples:**
```
Input: "1,2,2,3,1"     Output: "123" or [1,2,3]
Input: "1||1,,,,2"     Output: "12" or [1,2]
```

**Method Signature:**
```java
public String getUniqueDigits(String input) { }
public int[] getUniqueNumbers(String input) { }
```

---

## **A9: Filter Even/Odd**
**Problem:** Extract only even or odd digits/numbers.

**Examples:**
```
Input: "1,2,34,5"      Even digits: "24", Odd digits: "135"
Input: "1,2,34,5"      Even numbers: [2,34], Odd numbers: [1,5]
```

**Method Signature:**
```java
public String getEvenDigits(String input) { }
public int[] getOddNumbers(String input) { }
```

---

# 🔢 TASK B VARIATIONS (Numerical Operations)

## **B1: Sum Individual Digits** ⭐ MOST LIKELY
**Problem:** Sum all individual digits (not whole numbers).

**Examples:**
```
Input: "1,2,34"        Output: 10 (1+2+3+4)
Input: "1||2,,,,3"     Output: 6  (1+2+3)
Input: "-1,2,3"        Output: 6  (1+2+3)
```

**Method Signature:**
```java
public int sumDigits(String input) { }
```

---

## **B2: Sum Whole Numbers**
**Problem:** Sum all extracted whole numbers.

**Examples:**
```
Input: "1,2,34"        Output: 37 (1+2+34)
Input: "10||2,,,,30"   Output: 42 (10+2+30)
Input: "-1,2,34"       Output: 37 (1+2+34)
```

**Method Signature:**
```java
public long sumNumbers(String input) { }
```

---

## **B3: Count Elements**
**Problem:** Count digits, numbers, or delimiters.

**Examples:**
```
Input: "1,2,34"        Count digits: 4, Count numbers: 3, Count delimiters: 2
Input: "1||2,,,,3"     Count digits: 3, Count numbers: 3, Count delimiters: 6
```

**Method Signature:**
```java
public int countDigits(String input) { }
public int countNumbers(String input) { }
public int countDelimiters(String input) { }
```

---

## **B4: Product Operations**
**Problem:** Calculate product of digits or numbers.

**Examples:**
```
Input: "1,2,34"        Product digits: 24 (1×2×3×4), Product numbers: 68 (1×2×34)
Input: "2||3,,,,4"     Product digits: 24 (2×3×4), Product numbers: 24 (2×3×4)
```

**Method Signature:**
```java
public long productDigits(String input) { }
public long productNumbers(String input) { }
```

---

## **B5: Average/Mean**
**Problem:** Calculate average of digits or numbers.

**Examples:**
```
Input: "1,2,34"        Avg digits: 2.5 (10/4), Avg numbers: 12.33 (37/3)
Input: "2||4,,,,6"     Avg digits: 4.0 (12/3), Avg numbers: 4.0 (12/3)
```

**Method Signature:**
```java
public double averageDigits(String input) { }
public double averageNumbers(String input) { }
```

---

## **B6: Min/Max Operations**
**Problem:** Find minimum and maximum values.

**Examples:**
```
Input: "1,2,34"        Min digit: 1, Max digit: 4, Min number: 1, Max number: 34
Input: "5||1,,,,9"     Min digit: 1, Max digit: 9, Min number: 1, Max number: 9
```

**Method Signature:**
```java
public int minDigit(String input) { }
public int maxDigit(String input) { }
public int minNumber(String input) { }
public int maxNumber(String input) { }
```

---

## **B7: Mathematical Sequences**
**Problem:** Calculate mathematical properties like factorial sum, fibonacci-like operations.

**Examples:**
```
Input: "1,2,3"         Sum of factorials: 9 (1! + 2! + 3! = 1+2+6)
Input: "2,3,4"         Sum of squares: 29 (2²+3²+4² = 4+9+16)
```

**Method Signature:**
```java
public long sumFactorials(String input) { }
public long sumSquares(String input) { }
```

---

## **B8: Conditional Sums**
**Problem:** Sum only elements meeting certain criteria.

**Examples:**
```
Input: "1,2,34,5"      Sum even digits: 6 (2+4), Sum odd numbers: 6 (1+5)
Input: "12,13,24"      Sum if >10: 49 (12+13+24), Sum single digits: 0
```

**Method Signature:**
```java
public int sumEvenDigits(String input) { }
public int sumOddNumbers(String input) { }
public int sumNumbersAbove(String input, int threshold) { }
```

---

## **B9: Digital Root/Checksum**
**Problem:** Calculate digital root (keep summing digits until single digit) or checksum.

**Examples:**
```
Input: "1,2,34"        Digital root: 1 (1+2+3+4=10 → 1+0=1)
Input: "5,6,7"         Digital root: 9 (5+6+7=18 → 1+8=9)
```

**Method Signature:**
```java
public int digitalRoot(String input) { }
public int checksum(String input) { }
```

---

## **B10: Statistical Operations**
**Problem:** Calculate median, mode, standard deviation.

**Examples:**
```
Input: "1,2,3,4,5"     Median: 3, Mode: none (all appear once)
Input: "1,1,2,2,3"     Median: 2, Mode: 1 and 2 (tie)
```

**Method Signature:**
```java
public double median(String input) { }
public int[] mode(String input) { }
```

---

# 🧪 UNIVERSAL TEST CASES

**ALL variations must handle these edge cases:**

### **Input Validation:**
```java
"1a2"           → IllegalArgumentException
"1@2"           → IllegalArgumentException  
"abc"           → IllegalArgumentException
```

### **Delimiter Complexity:**
```java
"1||2,,,,3"     → Parse as [1,2,3]
"1|2,3;4 5"     → Parse as [1,2,3,4,5]
" ,,, || "      → Return appropriate empty value
```

### **Negative Handling:**
```java
"-1,2,3"        → Treat as [1,2,3]
"1,-2,3"        → Treat as [1,2,3]
"-1-2-3"        → Treat as [1,2,3]
```

### **Empty/Whitespace:**
```java
""              → Return appropriate empty value
"   "           → Return appropriate empty value
" 1 2 3 "       → Parse as [1,2,3]
```

---

# 🎯 STRATEGY BY PROBABILITY

## **HIGH PROBABILITY (Practice These First):**
- A1: Sort Digits Descending ⭐⭐⭐
- B1: Sum Individual Digits ⭐⭐⭐
- A3: Sort Numbers Descending ⭐⭐
- B2: Sum Whole Numbers ⭐⭐

## **MEDIUM PROBABILITY:**
- A5: Reverse Token Order ⭐
- B3: Count Elements ⭐
- A7: Get Largest/Smallest ⭐
- B6: Min/Max Operations ⭐

## **LOWER PROBABILITY (Advanced):**
- A8: Extract Unique Elements
- B7: Mathematical Sequences  
- B9: Digital Root/Checksum
- B10: Statistical Operations

---

# 🚀 IMPLEMENTATION APPROACH

For ANY variation, follow this pattern:

1. **Input Validation** (check allowed characters)
2. **Tokenization** (extract numbers/digits with delimiter handling)
3. **Core Logic** (sorting, summing, counting, etc.)
4. **Edge Case Handling** (empty, negatives, etc.)
5. **Return Appropriate Type** (String, int, int[], double, etc.)

**Remember:** The tokenization logic remains the same across all variations - only the processing changes!