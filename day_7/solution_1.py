from queue import Queue

input = open("./day_7/input.txt", "r").read()
equations = input.splitlines()

total_calibration_result = 0
for equation in equations:
    q = Queue()
    result, numbers = equation.split(": ")
    result_original = int(result)
    numbers = [int(n) for n in numbers.split(" ")]
    q.put((result_original, numbers))
    equation_valid = False
    while q.qsize() > 0:
        (result, numbers) = q.get()
        if len(numbers) == 0:
            continue
        if len(numbers) == 1 and result == numbers[0]:
            equation_valid = True
            break
        if result % numbers[-1] == 0:
            q.put((result // numbers[-1], numbers[:-1]))
        if result - numbers[-1] > 0:
            q.put((result - numbers[-1], numbers[:-1]))
    if equation_valid:
        total_calibration_result += result_original

print(total_calibration_result)