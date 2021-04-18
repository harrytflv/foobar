def solution(n):
	x = [[0 for i in range(n+1)] for j in range(n+1)]
	for j in range(0, n+1):
		x[0][j] = 0
	for i in range(2, n+1):
		for j in range (1, n+1):
			x[i][j] = x[i][j-1] + x[max(i-j, 0)][j-1] + (0 < i-j and i - j < j)
	return x[n][n]

def main():
    t = Test(solution)
    t.add_test_case(1, 3)
    t.add_test_case(2, 5)
    t.add_test_case(487067745, 200)
    t.run()

from datetime import datetime

class Test:
	def __init__(self, f):
		self.f = f
		self.test_cases = []

	def add_test_case(self, expected_out, *argv):
		self.test_cases.append((expected_out, argv))
	
	def run(self):
		start = datetime.now()

		passed = True
		for test_case in self.test_cases:
			res = self.f(*(test_case[1]))
			if res == test_case[0]:
				continue
			print("Input:           ", test_case[1])
			print("Expected Output: ", test_case[0])
			print("Output:          ", res)
			print()
			passed = False

		end = datetime.now()
		print(end - start)

		if passed:
			print("PASSED")

if __name__ == "__main__":
    main()
