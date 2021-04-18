def solution(start, num_of_workers):
	ret = 0
	for i in range(num_of_workers):
		head = start + i * num_of_workers
		num_of_current_line = num_of_workers - i
		tail = head + num_of_current_line - 1
		if (head % 2) == 0:
			remains = num_of_current_line % 4
			for i in range(remains):
				ret ^= tail
				tail -= 1
		else:
			ret ^= head
			remains = (num_of_current_line - 1) % 4
			for i in range(remains):
				ret ^= tail
				tail -= 1
	return ret

def slow_solution(start, num):
	counter, ret = start, 0
	for i in range(num):
		for j in range(num - i):
			ret ^= counter
			counter += 1
		counter += i
	return ret

def main():
    t = Test(solution)
    t.add_test_case(14, 17, 4)
    t.add_test_case(2, 0, 3)
    t.add_test_case(slow_solution(23, 89), 23, 89)
    t.add_test_case(slow_solution(12, 54), 12, 54)
    t.add_test_case(slow_solution(0, 2000), 0, 2000)
    # t.add_test_case(0, 0, 2000000000)
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
