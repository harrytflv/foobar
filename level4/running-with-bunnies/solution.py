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
    t.add_test_case([1, 2], [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
    t.add_test_case([0, 1], [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
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
log.toggle = False

if __name__ == "__main__":
    main()
