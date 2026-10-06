package main

import (
	"fmt"
	"sync/atomic"
)

const(
	maxValue = 1_000_000
	numThreads = 10
)

func count(tid int, counter *int32, done chan bool) {
	for i := 0; i < (maxValue / numThreads); i++ {
		for {
			current_value := *counter
			if atomic.CompareAndSwapInt32(counter, current_value, current_value + 1) {
				fmt.Printf("Thread %d: adding 1 to the counter count.\n", tid)
				break;
			}
		}
	}
	done <- true
}

func main() {
	var counter int32 = 0
	done := make(chan bool, 1)

	for i := 0; i < numThreads; i++ {
		go count(i, &counter, done)
	}

	for i := 0; i < numThreads; i++ {
		<- done
	}

	fmt.Printf("Counter value: %d | Expected value: %d\n", counter, maxValue)
}