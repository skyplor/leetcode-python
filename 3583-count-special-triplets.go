//go:build ignore

package main

import "fmt"

func specialTriplets(nums []int) int {
	mod := 1_000_000_007
	n := len(nums)
	prefix := make([]int, n)
	count := make(map[int]int)
	for j, num := range nums {
		prefix[j] = count[num*2]
		count[num]++
	}
	res := 0
	count = make(map[int]int)
	for j := n - 1; j >= 0; j-- {
		num := nums[j]
		suffix := count[num*2]
		res = (res + (prefix[j] * suffix)) % mod
		count[num]++
	}

	return res
}

func main() {
	fmt.Printf("Output: %d, expected: 1\n", specialTriplets([]int{6, 3, 6}))
	fmt.Printf("Output: %d, expected: 1\n", specialTriplets([]int{0, 1, 0, 0}))
	fmt.Printf("Output: %d, expected: 2\n", specialTriplets([]int{8, 4, 2, 8, 4}))
}
