//go:build ignore

package main

import "fmt"

func sumFourDivisors(nums []int) int {
	total := 0
	for _, n := range nums {
		temp_total := 0
		count := 0
		for i := 1; i*i <= n; i++ {
			if n%i == 0 {
				count++
				temp_total += i

				if i != n/i {
					count++
					temp_total += n / i
				}
			}
			if count > 4 {
				break
			}
		}
		if count == 4 {
			total += temp_total
		}
	}
	return total
}

func main() {
	fmt.Printf("Output: %d, expected: 32\n", sumFourDivisors([]int{21, 4, 7}))
	fmt.Printf("Output: %d, expected: 64\n", sumFourDivisors([]int{21, 21}))
	fmt.Printf("Output: %d, expected: 0\n", sumFourDivisors([]int{1, 2, 3, 4, 5}))
}
