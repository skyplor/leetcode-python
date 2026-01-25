//go:build ignore

package main

import "fmt"

func maximalRectangle(matrix [][]byte) int {
	n := len(matrix[0])
	maxArea := 0
	heights := make([]int, n+1)
	for _, row := range matrix {
		for col_i, col := range row {
			if col == '0' {
				heights[col_i] = 0
			} else {
				heights[col_i]++
			}
		}

		stack := make([][]int, 0)
		for i, h := range heights {
			prevI := i
			for len(stack) > 0 && (stack[len(stack)-1][1] > h) {
				top := stack[len(stack)-1]
				maxArea = max(maxArea, (i-top[0])*top[1])
				prevI = top[0]
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, []int{prevI, h})
		}

		for _, top := range stack {
			i, h := top[0], top[1]
			maxArea = max(maxArea, (n-i)*h)
		}
	}
	return maxArea
}

func main() {
	fmt.Printf("Output: %v, expected: 6\n", maximalRectangle([][]byte{{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}}))
	fmt.Printf("Output: %v, expected: 0\n", maximalRectangle([][]byte{{'0'}}))
	fmt.Printf("Output: %v, expected: 1\n", maximalRectangle([][]byte{{'1'}}))
}
