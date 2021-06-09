# -*- coding: utf-8 -*-

# https://gist.github.com/lotabout/891621ae8a01d8e512afd4b5254516b4

from collections import defaultdict

def transfer(col_1, col_2, height):
    col_1_no_tail = col_1 >> 1
    col_2_no_tail = col_2 >> 1
    col_1_no_head = col_1 & ~(1<<height)
    col_2_no_head = col_2 & ~(1<<height)

    # All four cases of one:
    # 1 0
    # 0 0
    tl =  col_1_no_tail & ~col_2_no_tail & ~col_1_no_head & ~col_2_no_head
    # 0 1
    # 0 0
    tr = ~col_1_no_tail &  col_2_no_tail & ~col_1_no_head & ~col_2_no_head
    # 0 0
    # 1 0
    bl = ~col_1_no_tail & ~col_2_no_tail &  col_1_no_head & ~col_2_no_head
    # 0 0
    # 0 1
    br = ~col_1_no_tail & ~col_2_no_tail & ~col_1_no_head &  col_2_no_head
    return tl | tr | bl | br

def solution(g):
    if len(g) == 0:
        return 0

    height, width = len(g), len(g[0])
    cols = [sum([1<<i if g[i][j] else 0 for i in range(height)]) for j in range(width)]

    # A mapping from (col_1, col_2) to a set containing col_3 means:
    #   col_1 = transfer(col_2, col_3)
    # The value of mapping[(col_a, col_b)] is all columns i such that:
    #   col_a = transfer(col_b, col_i)
    mapping = defaultdict(set)
    cols_set = set(cols)
    for col_pattern_a in range(1<<(height+1)):
        for col_pattern_b in range(1<<(height+1)):
            res = transfer(col_pattern_a, col_pattern_b, height)
            if res in cols_set:
                mapping[(res, col_pattern_a)].add(col_pattern_b)

    pre_state_col_num = {i: 1 for i in range(1<<(height+1))}
    for col in cols:
        pre_state_next_col_num = defaultdict(int)
        for col_1 in pre_state_col_num:
            for col_2 in mapping[(col, col_1)]:
                pre_state_next_col_num[col_2] += pre_state_col_num[col_1]
        pre_state_col_num = pre_state_next_col_num

    return sum(pre_state_col_num.values())

def slow_solution(g):
    if len(g) == 0:
        return 0

    class nebula_enumerator():
        def __init__(self, height, width):
            self.height = height
            self.width = width
            self.curr = 0

        def has_next(self):
            return self.curr <= 2 ** (self.height * self.width) - 1

        def next(self):
            nebula = [[0 for j in range(self.width)] for i in range(self.height)]
            curr_bin = bin(self.curr)[2:].zfill(self.height * self.width)

            for i in range(self.height):
                for j in range(self.width):
                    if curr_bin[i*self.width+j] == '0':
                        nebula[i][j] = 0
                    else:
                        nebula[i][j] = 1

            self.curr += 1

            return nebula

    enumerator, counter = nebula_enumerator(len(g)+1, len(g[0])+1), 0

    while enumerator.has_next():
        nebula = enumerator.next()
        after = [[0 for j in range(len(g[0]))] for i in range(len(g))]
        for i in range(len(g)):
            for j in range(len(g[0])):
                after[i][j] = 1 if nebula[i][j]+nebula[i][j+1]+nebula[i+1][j]+nebula[i+1][j+1] == 1 else 0
        if after == g:
            counter += 1

    return counter


def main():
    t = Test(solution)
    # for test_case in [
    #     [],
    # ]:
    #     t.add_test_case(slow_solution(test_case), test_case)
    t.add_test_case(0, [])
    t.add_test_case(12, [
        [0],
    ])
    t.add_test_case(4, [
        [1],
    ])
    t.add_test_case(10, [
        [1],
        [0],
    ])
    t.add_test_case(10, [
        [0],
        [1],
    ])
    t.add_test_case(10, [
        [1, 0],
    ])
    t.add_test_case(10, [
        [0, 1],
    ])
    t.add_test_case(6, [
        [1],
        [1],
    ])
    t.add_test_case(6, [
        [1, 1],
    ])
    t.add_test_case(8, [
        [1, 1, 1],
    ])
    t.add_test_case(8, [
        [1],
        [1],
        [1]
    ])
    t.add_test_case(12, [
        [1, 0],
        [0, 1]
    ])
    t.add_test_case(8, [
        [1, 1],
        [1, 1],
    ])
    t.add_test_case(4, [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ])
    t.add_test_case(254, [
        [1, 0, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1]
    ])
    t.add_test_case(11567, [
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
    ])
    t.add_test_case(10, [
        [False],
        [True],
    ])
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

def log(*args):
    if not log.toggle:
        return
    log.counter += 1
    if log.counter <= log.limit:
        if len(args) == 1:
            print(args[0])
        else:
            print(args)
log.limit = 100
log.counter = 0
log.toggle = True

if __name__ == "__main__":
    main()
