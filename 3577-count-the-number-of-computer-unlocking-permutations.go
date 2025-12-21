//go:build ignore

package main

import "fmt"

func countPermutations(complexity []int) int {
	first := complexity[0]
	for i := 1; i < len(complexity); i++ {
		if complexity[i] <= first {
			return 0
		}
	}
	res := 1
	for i := 1; i < len(complexity); i++ {
		res = (res * i) % 1_000_000_007
	}
	return res
}

func main() {
	fmt.Printf("Output: %d, expected: 2\n", countPermutations([]int{1, 2, 3}))
	fmt.Printf("Output: %d, expected: 0\n", countPermutations([]int{3, 3, 3, 4, 4, 4}))
	fmt.Printf("Output: %d, expected: 789741546\n", countPermutations([]int{38, 223, 100, 123, 406, 234, 256, 93, 222, 259, 233, 69, 139, 245, 45, 98, 214}))
}
