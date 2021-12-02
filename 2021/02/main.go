package main

import (
	"fmt"
	"bufio"
	"os"
    "strconv"
	"strings"
)

func get_readings(file *os.File) []string {
	var readings []string

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		readings = append(readings, line)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
	
	return readings
}

func main() {
	readings := get_readings(os.Stdin)

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

	fmt.Println("###Part 1###")
	fmt.Println("Depth:", depth)
	fmt.Println("Horizontal position:", horizontal_position)
	fmt.Println("Product:", depth * horizontal_position)

	// Part 2
	depth = 0
	horizontal_position = 0
	aim := 0

	for _, element := range readings {
		s := strings.Split(element, " ")

		direction := s[0]
		amount, _ := strconv.Atoi(s[1])

		if direction == "forward" {
			horizontal_position += amount
			depth += aim * amount
		}
		if direction == "up" {
			aim -= amount
		}
		if direction == "down" {
			aim += amount
		}
	}

	fmt.Println("###Part 2###")
	fmt.Println("Depth:", depth)
	fmt.Println("Horizontal position:", horizontal_position)
	fmt.Println("Product:", depth * horizontal_position)
}
