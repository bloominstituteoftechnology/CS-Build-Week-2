// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the jumpingOnClouds function below.
func jumpingOnClouds(c []int32) int32 {
	cntHops := 0
	cldNextNext := 0
	idx := 0

	// Iterate through the
	for idx < len(c) {
		fmt.Println("Hop:", idx)

		// Are we on the last cloud?
		if idx == len(c)-1 {
			// yes: done processing
			break
		}

		// Determine next two cloud indexes (numbers)
		cldNextNext = -999
		if idx < len(c)-2 {
			// Determine the next-next cloud if it exists
			cldNextNext = idx + 2
		}

		// Is next-next cloud a cumulus cloud?
		if cldNextNext != -999 && c[cldNextNext] == 0 {
			// yes: the next-next cloud exists and is "safe"
			cntHops = cntHops + 1 // increase cloud hop by 1
			idx = cldNextNext
			continue
		}

		// Only option is to jump on the next cloud (assume "safe")
		cntHops = cntHops + 1 // increase cloud hop by 1
		idx = idx + 1         // shift to the next-next cloud
	}

	// return the number of hops
	return int32(cntHops)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	cTemp := strings.Split(readLine(reader), " ")

	var c []int32

	for i := 0; i < int(n); i++ {
		cItemTemp, err := strconv.ParseInt(cTemp[i], 10, 64)
		checkError(err)
		cItem := int32(cItemTemp)
		c = append(c, cItem)
	}

	result := jumpingOnClouds(c)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
