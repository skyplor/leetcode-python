//go:build ignore

package main

import (
	"cmp"
	"fmt"
	"slices"
	"strconv"
	"strings"
)

func countMentions(numberOfUsers int, events [][]string) []int {
	slices.SortFunc(events, func(e1, e2 []string) int {
		time1, _ := strconv.Atoi(e1[1])
		time2, _ := strconv.Atoi(e2[1])
		if time1 == time2 {
			return cmp.Compare(e2[0], e1[0])
		}
		return cmp.Compare(time1, time2)
	})

	mentions := make([]int, numberOfUsers)
	onlineTimeOffset := 60
	usersOnlineTime := make([]int, numberOfUsers)
	allMentioned := 0

	for _, event := range events {
		eventType, time, users := event[0], event[1], event[2]
		if eventType == "MESSAGE" {
			if users == "HERE" {
				for user, onlineTime := range usersOnlineTime {
					timeInt, _ := strconv.Atoi(time)
					if timeInt >= onlineTime {
						mentions[user]++
					}
				}
				continue
			}
			if users == "ALL" {
				allMentioned++
				continue
			}
			userList := strings.Split(users, " ")
			for _, user := range userList {
				userId, _ := strconv.Atoi(user[2:])
				mentions[userId]++
			}
			continue
		}
		userId, _ := strconv.Atoi(users)
		timeInt, _ := strconv.Atoi(time)
		usersOnlineTime[userId] = timeInt + onlineTimeOffset
	}
	for user := range numberOfUsers {
		mentions[user] += allMentioned
	}

	return mentions
}

func main() {
	fmt.Printf("Output: %v, expected: [2, 2]\n", countMentions(2, [][]string{{"MESSAGE", "10", "id1 id0"}, {"OFFLINE", "11", "0"}, {"MESSAGE", "71", "HERE"}}))
	fmt.Printf("Output: %v, expected: [2, 2]\n", countMentions(2, [][]string{{"MESSAGE", "10", "id1 id0"}, {"OFFLINE", "11", "0"}, {"MESSAGE", "12", "ALL"}}))
	fmt.Printf("Output: %v, expected: [2, 2]\n", countMentions(2, [][]string{{"OFFLINE", "10", "0"}, {"MESSAGE", "12", "HERE"}}))
}
