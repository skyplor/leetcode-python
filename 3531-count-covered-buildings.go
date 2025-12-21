//go:build ignore

package main

import (
	"fmt"
	"math"
)

func countCoveredBuildings(n int, buildings [][]int) int {
	minY := make([]int, n+1)
	minX := make([]int, n+1)
	maxY := make([]int, n+1)
	maxX := make([]int, n+1)

	for i := range n + 1 {
		minY[i] = math.MaxInt
		minX[i] = math.MaxInt
	}

	for _, building := range buildings {
		x, y := building[0], building[1]

		minY[x] = min(minY[x], y)
		maxY[x] = max(maxY[x], y)
		minX[y] = min(minX[y], x)
		maxX[y] = max(maxX[y], x)
	}

	res := 0
	for _, building := range buildings {
		x, y := building[0], building[1]
		if minX[y] < x && x < maxX[y] && minY[x] < y && y < maxY[x] {
			res++
		}
	}

	return res
}

func main() {
	fmt.Printf("Output: %d, expected: 1\n", countCoveredBuildings(3, [][]int{{1, 2}, {2, 2}, {3, 2}, {2, 1}, {2, 3}}))
	fmt.Printf("Output: %d, expected: 0\n", countCoveredBuildings(3, [][]int{{1, 1}, {1, 2}, {2, 1}, {2, 2}}))
	fmt.Printf("Output: %d, expected: 1\n", countCoveredBuildings(5, [][]int{{1, 3}, {3, 2}, {3, 3}, {3, 5}, {5, 3}}))
	fmt.Printf("Output: %d, expected: 0\n", countCoveredBuildings(3, [][]int{{1, 1}, {1, 2}, {1, 3}}))
}
