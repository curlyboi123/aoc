package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
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

func get_most_common_bit(bits [][]string, position int) map[string]int {
	zero_count := 0
	one_count := 0

	for _, bit := range(bits) {
		if bit[position] == "0" {
			zero_count ++
		}
		if bit[position] == "1" {
			one_count ++
		}
	}

	return map[string]int{"0": zero_count, "1": one_count}
}

func part_one(readings []string) {
	var bits [][]string

	// Get list of lists of bits in each number
	for _, line := range(readings) {
		bit := strings.Split(line, "")
		bits = append(bits, bit)
	}

	// Get list of maps of how much each bit appeared
	var most_common_bits []map[string]int
	for i := 0; i < len(bits[0]); i++ {
		individual_most_common_bit := get_most_common_bit(bits, i)
		most_common_bits = append(most_common_bits, individual_most_common_bit)
	}

	// Get most and least common bit in each position
	var most_common_bit string
	var least_common_bit string

	for _, bit_mode := range(most_common_bits) {
		if bit_mode["0"] > bit_mode["1"] {
			most_common_bit += "0"
			least_common_bit += "1"
		}
		if bit_mode["0"] < bit_mode["1"]{
			most_common_bit += "1"
			least_common_bit += "0"
		}
	}

	fmt.Println("Most common bit: ", most_common_bit)
	gamma_rate, _ := strconv.ParseInt(most_common_bit, 2, 64)
	fmt.Println("Gamma rate: ", gamma_rate)

	fmt.Println("Least common bit: ", least_common_bit)
	epsilon_rate, _ := strconv.ParseInt(least_common_bit, 2, 64)
	fmt.Println("Epsilon rate: ", epsilon_rate)

	power_consumption := gamma_rate * epsilon_rate
	fmt.Println("Power consumption: ", power_consumption)
}


func part_two(readings []string) {
	bit_mode := make(map[string]int)
	for _, line := range(readings) {
		bit := string(line[0])
		bit_mode[bit] ++
		
	}

	if bit_mode["0"] > bit_mode["1"] {
		most_common_bit += "0"
		least_common_bit += "1"
	}
	if bit_mode["0"] < bit_mode["1"] || bit_mode["0"] == bit_mode["1"] { // TODO change to else?
		most_common_bit += "1"
		least_common_bit += "0"
	}
}


func main() {
	readings := get_readings(os.Stdin)

	// part_one(readings)
	part_two(readings)

	// Part 2
	// oxygen_generator_rating, _ := strconv.ParseInt(most_common_part_two_bit, 2, 64)
	// fmt.Println("Oxygen generator rating: ", oxygen_generator_rating)

	// co2_scrubber_rating, _ := strconv.ParseInt(least_common_part_two_bit, 2, 64)
	// fmt.Println("CO2 scrubber rating: ", co2_scrubber_rating)
}
