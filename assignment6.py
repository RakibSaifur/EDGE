#Index position of a string
sample_string = "google.com"
frequency = {}

for char in sample_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:", frequency)
