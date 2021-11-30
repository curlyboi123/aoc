package main

import "fmt"
import "io/ioutil"
import "strings"

func main() {
    // Get slice of expense report
    b, err := ioutil.ReadFile("expense_report_short.txt")
    if err != nil {
        fmt.Print(err)
    }

    expense_report := strings.Split(string(b), "\n")
    fmt.Println(expense_report)

    // Get sums of comibnations
}
