package staircase

import (
	"testing"
)

func TestSolution(t *testing.T) {
	if solution(200) != 487067745 {
		t.Error("Wrong!")
	}
}
