import csv
# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

csv_file_path1 = os.path.join(cwd, "./csv", 'letters_lower.csv')
csv_file_path2 = os.path.join(cwd, "./csv", 'letters_upper.csv')
csv_file_path3 = os.path.join(cwd, "./csv", 'numbers.csv')
csv_file_path4 = os.path.join(cwd, "./csv", 'special_chars.csv')

# Generate set of lowercase letters
letters_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]

# Generate set of uppercase letters
letters_upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]

# Generate set of numbers
numbers = [str(i) for i in range(10)]

# Generate set of special characters
special_chars = [chr(i) for i in range(32, 127) if i not in range(ord('A'), ord('Z')+1) and i not in range(ord('a'), ord('z')+1) and i not in range(ord('0'), ord('9')+1)]

# Write lowercase letters to a CSV file
with open(csv_file_path1, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(letters_lower)

# Write uppercase letters to a CSV file
with open(csv_file_path2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(letters_upper)

# Write numbers to a CSV file
with open(csv_file_path3, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(numbers)

# Write special characters to a CSV file
with open(csv_file_path4, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(special_chars)
