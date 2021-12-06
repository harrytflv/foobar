package staircase

func solution(n int) int {
	x := make([][]int, n+1)
	for i := range x {
		x[i] = make([]int, n+1)
	}

	for i := 0; i <= n; i++ {
		for j := 1; j <= n; j++ {
			x[i][j] = x[i][j-1] + x[max(i-j, 0)][j-1]
			if 0 < i-j && i-j < j {
				x[i][j]++
			}
		}
	}

	return x[n][n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
