//go:build ignore

package main

import "fmt"

func minDeletionSize(strs []string) int {
	toDel := 0
	checkList := make([]int, len(strs)-1)
	for i := 0; i < len(strs)-1; i++ {
		checkList = append(checkList, i)
	}

	for j := 0; j < len(strs[0]); j++ {
		var newChecklist []int
		shouldDelete := false

		for _, i := range checkList {
			if strs[i][j] > strs[i+1][j] {
				toDel++
				shouldDelete = true
				break
			}
			if strs[i][j] == strs[i+1][j] {
				newChecklist = append(newChecklist, i)
			}
		}
		if !shouldDelete {
			if len(newChecklist) == 0 {
				return toDel
			}
			checkList = newChecklist
		}
	}
	return toDel
}

func main() {
	fmt.Printf("output: %d, expected: 1\n", minDeletionSize([]string{"ca", "bb", "ac"}))
	fmt.Printf("output: %d, expected: 0\n", minDeletionSize([]string{"xc", "yb", "za"}))
	fmt.Printf("output: %d, expected: 3\n", minDeletionSize([]string{"zyx", "wvu", "tsr"}))
}
