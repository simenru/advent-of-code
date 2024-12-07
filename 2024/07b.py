data = []
with open("inputs/07.txt") as input:
    for line in input:
        line = line.strip()
        test_value, numbers = line.split(": ")
        numbers = numbers.split(" ")
        test_value, numbers = int(test_value), [int(number) for number in numbers]
        data.append((test_value, numbers))

def can_result_in(test_value, numbers):
    if len(numbers) == 1:
        return test_value == numbers[0]
    #elif numbers[0] > test_value:
    #    return False
    else:
        return can_result_in(test_value, [numbers[0] + numbers[1]] + numbers[2:]) | can_result_in(test_value, [numbers[0] * numbers[1]] + numbers[2:]) | can_result_in(test_value, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])


sum = 0
for test_value, numbers in data:
    if can_result_in(test_value, numbers):
        sum += test_value

print(sum)