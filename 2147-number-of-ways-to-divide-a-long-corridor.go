//go:build ignore

package main

import (
	"fmt"
	"strings"
)

func numberOfWays(corridor string) int {
	groupingMap := map[int]int{0: 1, 1: 2, 2: 1}
	sCount := strings.Count(corridor, "S")
	if sCount < 2 || sCount%2 != 0 {
		return 0
	}

	groupings := make([]int, len(corridor))
	for i, ch := range corridor {
		if i == 0 {
			groupings[i] = 0
			if ch == 'S' {
				groupings[i] = 1
			}
			continue
		}
		if ch == 'P' {
			groupings[i] = groupings[i-1]
			continue
		}
		groupings[i] = groupingMap[groupings[i-1]]
	}

	right, res, left := 1, 1, 0
	for right < len(corridor)-1 {
		prev, curr := groupings[right-1], groupings[right]
		if prev == 1 && curr == 2 {
			multiplier := 1
			left = right
			if groupings[right] == 2 {
				for right < len(corridor) && groupings[right] == 2 {
					right++
				}
				if right < len(corridor)-1 {
					multiplier = right - left
				}
				res = (res * multiplier) % (1_000_000_007)
			}
		}
		right++
	}

	return res
}

func main() {
	fmt.Printf("Output: %v, expected: 3\n", numberOfWays("SSPPSPS"))
	fmt.Printf("Output: %v, expected: 1\n", numberOfWays("PPSPSP"))
	fmt.Printf("Output: %v, expected: 0\n", numberOfWays("S"))
}
