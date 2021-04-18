def solution(l):
    l.sort()
    sum_of_nums = sum(l)

    if sum_of_nums % 3 == 0:
        l.reverse()
        return int("".join(map(lambda x: str(x), l)))

    if len(l) == 1:
        return 0
    for val in l:
        if val % 3 == sum_of_nums % 3:
            l.remove(val)
            l.reverse()
            return int("".join(map(lambda x: str(x), l)))

    if len(l) == 2:
        return 0
    for i in range(1,len(l)):
        for j in range(0, i):
            if (l[i] + l[j]) % 3 == sum_of_nums % 3:
                l.remove(l[i])
                l.remove(l[j])
                l.reverse()
                return int("".join(map(lambda x: str(x), l)))

    return 0

def main():
    t = Test(solution)
    t.add_test_case(0, [0])
    t.add_test_case(0, [1])
    t.add_test_case(0, [1, 1])
    t.add_test_case(21, [1, 2])
    t.add_test_case(3, [1, 1, 3])
    t.add_test_case(3, [1, 3, 4])
    t.add_test_case(93, [1, 3, 4, 9])
    t.add_test_case(930, [1, 3, 4, 9, 0])
    t.add_test_case(930, [1, 3, 4, 9, 0])
    t.add_test_case(4311, [3, 1, 4, 1])
    t.add_test_case(94311, [3, 1, 4, 1, 5, 9])
    t.add_test_case(999999999, [9, 9, 9, 9, 9, 9, 9, 9, 9])
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
