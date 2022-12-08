#Import CSV to be able to use csv functions
import csv
import string

def parse_input(filename):
    # create an empty dictionary to store the results
    results = {}

    # open the file and read the contents
    with open(filename, 'r') as f:
        text = f.read()

    # iterate over each character in the text
    for char in text:
        # check if the character is a letter, number, or special character
        if char in string.ascii_letters + string.digits + string.punctuation:
            # if the character is already in the dictionary, increment its count
            if char in results:
                results[char] += 1
            # otherwise, add the character to the dictionary with a count of 1
            else:
                results[char] = 1

    # calculate the total number of characters
    total_chars = sum(results.values())

    # iterate over each character and its count in the dictionary
    for char, count in results.items():
        # calculate the percentage of the total number of characters
        percentage = count / total_chars * 100
        # add the character, count, and percentage to the results dictionary
        results[char] = (count, percentage)

    return results

def write_to_csv(results, filename):
    # open the output file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Character", "Occurrence", "Percentage"], delimiter="\t")
        # Write the header row
        writer.writeheader()
        # Iterate over each character and its count and percentage in the results
        for char, data in results.items():
            count, percentage = data
            # Write the character, count, and percentage to the output file
            writer.writerow({"Character": f"{char}", "Occurrence": count, "Percentage": percentage})

# parse the input from the text file
results = parse_input('teest.txt')
# write the results to a CSV file
write_to_csv(results, 'charcount.csv')