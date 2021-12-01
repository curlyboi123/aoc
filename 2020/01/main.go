package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

func main() {
    target_number := 2020
    expense_report_filename := "expense_report_long.txt"

    // Get slice of expense report
    b, err := ioutil.ReadFile(expense_report_filename)
    if err != nil {
        fmt.Print(err)
    }

    expense_report := strings.Split(string(b), "\n")

    // Get sums of pairs of numbers
    for i := 0; i < len(expense_report) - 1; i++ {
        for j := i+1; j < len(expense_report); j++ {
            num_1, _ := strconv.Atoi(expense_report[i])
            num_2, _ := strconv.Atoi(expense_report[j])

            total := num_1 + num_2

            if total == target_number {
                fmt.Println("The numbers that add to equal", target_number, "are", num_1, "and", num_2)
                fmt.Println("The positions of these numbers in the slice are", i, "and", j)
                fmt.Println("The product of these two numbers is", num_1 * num_2)
            }
        }   
    } 
}
