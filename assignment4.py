#finding the second largest number of a list
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1]
numbers = [5, 8, 2, 10, 3]
result = second_largest(numbers)
print("The second largest number is:", result)
