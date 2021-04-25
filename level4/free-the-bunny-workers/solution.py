import itertools

def solution(num_buns, num_required):
    combinations_of_bunnies = list(itertools.combinations(range(num_buns), num_buns - num_required + 1))
    return [filter(lambda x: bunny_i in combinations_of_bunnies[x] != 0, range(len(combinations_of_bunnies))) for bunny_i in range(num_buns)]

def main():
    t = Test(solution)
    t.add_test_case([[]], 1, 0)
    t.add_test_case([[0]], 1, 1)
    t.add_test_case([[], []], 2, 0)
    t.add_test_case([[], []], 2, 3)
    t.add_test_case([[0], [0]], 2, 1)
    t.add_test_case([[0, 1], [0, 2], [1, 2]], 3, 2)
    t.add_test_case([[0], [1], [2], [3]], 4, 4)
    t.add_test_case([[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 4, 2)
    t.add_test_case([[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]], 5, 3)
    t.run()

from datetime import datetime
import copy

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
            res = self.f(*(copy.deepcopy(test_case[1])))
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
