import matplotlib.pyplot as plt
import csv

# Open the file and read the data
with open("charcount.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter="\t")

    # Skip the header row
    next(reader)

    # Read the data into a list of tuples, checking each value
    # to make sure it can be converted to the correct data type
    data = [(row[0], int(row[1]) if row[1].isnumeric() else 0, float(row[2]) if row[2].isdecimal() else 0.0) for row in reader]

# Extract the letters, the number of occurrences, and the percentages
# into separate lists
character, occurrences, percentages = zip(*data)

# Create the figure and two subplots
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Create the bar graph for the number of occurrences
# on the first subplot
ax1.bar(character, occurrences, color="blue", width=2)

# Set the y-axis limit for the first subplot
ax1.set_ylim(0, (max(occurrences)+(max(occurrences)/10)))

# Create the bar graph for the percentages
# on the second subplot
ax2.bar(character, percentages, color="red", width=0.5)

# Set the y-axis limit for the second subplot
ax2.set_ylim(0, (max(percentages)+(max(percentages)/10)))
print(max(percentages))
print(max(percentages)/10)
print((max(percentages)+(max(percentages)/10)))
# Add labels and title to the graph
ax1.set_xlabel("Letter")
ax1.set_ylabel("Number of Occurrences")
ax2.set_ylabel("Percentage")
plt.title("Number of Occurrences and Percentage for Each Letter")

# Show the graph
plt.show()
