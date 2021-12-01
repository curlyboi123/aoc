package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

func main() {
    filename := "depth_measurements_long.txt"

    // Get slice of expense report
    b, err := ioutil.ReadFile(filename)
    if err != nil {
        fmt.Print(err)
    }

    filename_slice := strings.Split(string(b), "\n")

	num_of_increases := 0

	for i := 1; i < len(filename_slice); i++ {
		current_value, _ := strconv.Atoi(filename_slice[i])
		previous_value, _ := strconv.Atoi(filename_slice[i - 1])

		if current_value > previous_value {
			num_of_increases += 1
		}
	}

	fmt.Println(num_of_increases)
}
