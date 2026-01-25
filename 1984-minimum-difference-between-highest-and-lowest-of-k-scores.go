//go:build ignore

package main

import (
	"fmt"
	"math"
	"slices"
)

func minimumDifference(nums []int, k int) int {
	slices.Sort(nums)
	minDiff := math.MaxInt32
	for i := 0; i < len(nums)-k+1; i++ {
		currDiff := nums[i+k-1] - nums[i]
		if currDiff < minDiff {
			minDiff = currDiff
		}
	}

	return minDiff
}

func main() {
	fmt.Printf("Output: %v, expected: 0\n", minimumDifference([]int{90}, 1))
	fmt.Printf("Output: %v, expected: 2\n", minimumDifference([]int{9, 4, 1, 7}, 2))
}
