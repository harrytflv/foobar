import functools 

def solution(xs):
    non_zeros = filter(lambda x: x != 0, xs)
    if len(non_zeros) == 0:
        return "0"
    if len(non_zeros) == 1 and non_zeros[0] < 0:
        if len(xs) - len(non_zeros) == 0:
            return str(non_zeros[0])
        return "0"
    numbers = non_zeros
    negatives = filter(lambda x: x < 0, xs)
    if len(negatives) % 2 != 0:
        max_negative_i = numbers.index(max(negatives))
        numbers = numbers[:max_negative_i]+numbers[max_negative_i+1:]
    if len(numbers) == 0:
        return "0"
    return str(functools.reduce(lambda a,b : a*b, numbers))

print(solution([2, 0, 2, 2, 0])=="8")
print(solution([-2, -3, 4, -5])=="60")
print(solution([-2, 0])=="0")
print(solution([-2, 1])=="1")
print(solution([0])=="0")
print(solution([0, 0])=="0")
print(solution([-1])=="-1")
print(solution([-1, -1])=="1")
print(solution([-1, -1, -1])=="1")
print(solution([1])=="1")
print(solution([
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    -1000,
    -1000,
    -1000,
    1000,
]))
