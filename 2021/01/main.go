package main

import (
	"fmt"
    "strconv"
	"bufio"
	"os"
)

func main() {
	var readings []int

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		readings = append(readings, num)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	// Part 1
	single_value_increases := 0
	for i := 1; i < len(readings); i++ {
		if readings[i] > readings[i - 1] {
			single_value_increases += 1
		}
	}
	fmt.Println("(Part 1) Single value increases", single_value_increases)

	fmt.Println(num_of_increases)
}
