#Changing even position of a string to uppercase letter
def change_even_position_to_uppercase(input_string):
    modified_string = list(input_string)
    for i in range(1, len(modified_string), 2):
        modified_string[i] = modified_string[i].upper()
    return ''.join(modified_string)
user_input = input("Enter a string")
result = change_even_position_to_uppercase(user_input)
print("Modified string:", result)