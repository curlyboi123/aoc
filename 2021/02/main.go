package main

import (
	"fmt"
	"bufio"
	"os"
    "strconv"
	"strings"
)

func main() {
	// Move to common module
	var readings []string

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		readings = append(readings, line)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	// Part 1
	depth := 0
	horizontal_position := 0

	for _, element := range readings {
		s := strings.Split(element, " ")

		direction := s[0]
		distance_moved, _ := strconv.Atoi(s[1])

		if direction == "forward" {
			horizontal_position += distance_moved
		}
		if direction == "up" {
			depth -= distance_moved
		}
		if direction == "down" {
			depth += distance_moved
		}
	}

	fmt.Println("Depth:", depth)
	fmt.Println("Horizontal position:", horizontal_position)

	fmt.Println("Product:", depth * horizontal_position)
}
