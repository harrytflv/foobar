from itertools import permutations

def solution(times, times_limit):
    number_of_points, start, bulkhead = len(times), 0, len(times)-1

    def path_to_bunnies(path):
        points = path[1:-1]
        points.sort()
        return map(lambda x: x-1, points)

    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    for k in range(number_of_points):
        for i in range(number_of_points):
            for j in range(number_of_points):
                times[i][j] = min(times[i][k] + times[k][j], times[i][j])
    for point_i in range(number_of_points):
        if times[point_i][point_i] < 0:
            return path_to_bunnies(range(number_of_points))

    curr_best_path = [start]
    for path in permutations(range(number_of_points)[1:-1]):
        curr_times, curr_path = 0, [start]
        for point_i in path:
            if curr_times + times[curr_path[-1]][point_i] + times[point_i][bulkhead] <= times_limit:
                curr_times += times[curr_path[-1]][point_i]
                curr_path.append(point_i)
                if len(curr_path) == number_of_points-1:
                    break
            else:
                break
        if len(curr_path) > len(curr_best_path):
            curr_best_path = curr_path
    curr_best_path.append(bulkhead)

    return path_to_bunnies(curr_best_path)


def slow_solution(times, times_limit):
    # A footprint for a vertex along the path is the set of visited vertices
    # when visiting that vertex.
    # For example, for path A->B->A->C, the footprint at the first A is A, the
    # footprint at B is AB, and the footprint at the second A is AB.
    # By avoiding same footprint, we are avoiding paths like A->B->A->B->C while
    # allowing A->B->A->C.
    class FootPrint:
        def __init__(self, visited, sum_of_weights):
            self.visited = visited
            self.sum_of_weights = sum_of_weights

    class Path:
        def __init__(self, prev_path, curr_vertex, sum_of_weights, visited):
            self.curr_vertex = curr_vertex
            self.sum_of_weights = sum_of_weights
            self.visited = visited
            self.path = prev_path[:]
            self.path.append(curr_vertex)

        def __str__(self):
            return "{0} {1} {2} {3}".format(self.curr_vertex, self.path, self.sum_of_weights, self.visited.keys())

        # 1 means we aren't stepping on the same footprint.
        # 0 means yes.
        # -1 means a negative cycle is detected.
        def compare_target_against_footprint(self, vertex):
            if vertex not in self.visited:
                return 1
            footprint = self.visited[vertex]
            if len(footprint.visited) < len(self.visited):
                return 1
            if times[self.curr_vertex][vertex] + self.sum_of_weights >= footprint.sum_of_weights:
                return 0
            return -1

        def visit(self, vertex):
            new_visited_vertices = set(self.visited.keys())
            new_visited_vertices.add(vertex)
            new_footprint = FootPrint(new_visited_vertices, self.sum_of_weights + times[self.curr_vertex][vertex])
            new_visted = self.visited.copy()
            new_visted[vertex] = new_footprint
            return Path(self.path, vertex, self.sum_of_weights + times[self.curr_vertex][vertex], new_visted)

    paths, unfinished_paths = [], [Path([], 0, 0, {0: FootPrint({0}, 0)})]
    while len(unfinished_paths):
        curr_path = unfinished_paths.pop()
        for i in range(len(times)):
            if i == curr_path.curr_vertex:
                continue
            if curr_path.compare_target_against_footprint(i) == 0:
                continue
            if curr_path.compare_target_against_footprint(i) == -1:
                return map(lambda x: x-1, range(len(times)))[1:-1]
            if curr_path.compare_target_against_footprint(i) == 1:
                new_path = curr_path.visit(i)
                if i == len(times) - 1:
                    if new_path.sum_of_weights <= times_limit:
                        paths.append(new_path)
                unfinished_paths.append(new_path)

    def compare_paths(path_1, path_2):
        if len(path_1.visited) < len(path_2.visited):
            return 1
        if len(path_1.visited) > len(path_2.visited):
            return -1
        path_1_visited = sorted(path_1.visited.keys())
        path_2_visited = sorted(path_2.visited.keys())
        for i in range(len(path_1_visited)):
            if path_1_visited[i] > path_2_visited[i]:
                return 1
            if path_1_visited[i] < path_2_visited[i]:
                return -1
        return 0

    if len(paths) == 0:
        return []
    path = sorted(paths, compare_paths)[0]
    return map(lambda x: x-1, sorted(path.visited.keys())[1:-1])

def main():
    t = Test(solution)
    t.add_test_case([], [[0, 1], [1, 0]], 0)
    t.add_test_case([], [[0, 1], [1, 0]], 2)
    t.add_test_case([], [[0, 1, 10], [10, 0, 1], [10, 10, 0]], 0)
    t.add_test_case([0], [[0, 1, 10], [10, 0, 1], [10, 10, 0]], 2)
    t.add_test_case([0], [[0, 1, 10], [-2, 0, 10], [10, 10, 0]], 0)
    t.add_test_case([0, 1], [[0, 10, 0, 10], [10, 0, 10, 0], [10, 0, 0, 10], [10, 10, 10, 0]], 0)
    t.add_test_case([1, 2], [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
    t.add_test_case([0, 1], [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
    t.add_test_case([0, 1, 2, 3, 4], [
        [0, 12, 4, 1, 2, 3, 3],
        [0, 0, 3, 8, 3, 7, 8],
        [1, 14, 0, 2, 6, 4, 2],
        [6, 1, 3, 0, 9, 7, 2],
        [0, 2, 4, 1, 0, 3, 6],
        [8, 23, 4, 9, 2, 0, 3],
        [6, 8, 6, 7, 2, 3, 0],
    ], 999)
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
log.limit = 20
log.counter = 0
log.toggle = True

if __name__ == "__main__":
    main()
