import csv
import matplotlib.pyplot as plt

# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the file path for the CSV file using the current working directory
# and a relative path to the "csv" directory
csv_file_path1 = os.path.join(cwd, "./csv", 'charcount.csv')
csv_file_path2 = os.path.join(cwd, "./csv", 'digraphcount.csv')

# read the data from the csv file
data = {}
with open(csv_file_path1, 'r') as f:
    reader = csv.reader(f)
    
    # skip the first line (header)
    next(reader)
    
    # read each line and extract the character, occurrence, and percentage
    for line in reader:
        character, occurrence, percentage = line
        data[character] = (int(occurrence), float(percentage))

# sort the data in descending order by occurrence
sorted_data = sorted(data.items(), key=lambda x: x[1][0], reverse=True)

# extract the character, occurrence, and percentage data
characters = [c[0] for c in sorted_data]
occurrences = [c[1][0] for c in sorted_data]
percentages = [c[1][1] for c in sorted_data]

# create a figure with a specific size
fig = plt.figure(figsize=(20, 10))

# create the bar graph with two y-axes
ax1 = plt.subplot()

# create the first y-axis for the occurrences data
ax1.bar(characters, occurrences, color='b')
ax1.set_xlabel('Character')
ax1.set_ylabel('Occurrences', color='b')
ax1.tick_params('y', colors='b')

# create the second y-axis for the percentages data
ax2 = ax1.twinx()
ax2.plot(characters, percentages, color='r')
ax2.set_ylabel('Percentages', color='r')
ax2.tick_params('y', colors='r')

# set the y-limits to be 110% of the maximum value
max_occurrences = max(occurrences)
max_percentages = max(percentages)
ax1.set_ylim(0, max_occurrences * 1.1)
ax2.set_ylim(0, max_percentages * 1.1)

# set the locations and labels of the x-axis ticks
ax1.set_xticks(range(len(characters)))
ax1.set_xticklabels(characters)

# rotate the x-axis labels to make them vertical
plt.xticks(rotation=90)

# add padding between the subplot and the figure
plt.subplots_adjust(bottom=0.15, top=0.9)

# show the first plot
plt.show()


# read the data from the csv file
data = {}
with open(csv_file_path2, 'r') as f:
    reader = csv.reader(f)
    
    # skip the first line (header)
    next(reader)
    
     # read each line and extract the digraph, occurrence
    for line in reader:
        digraph, occurrence = line
        data[digraph] = int(occurrence)

# sort the data sort the data in descending order by occurrence
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

#extract the digraph and occurrence data
digraphs = [d[0] for d in sorted_data]
occurrences = [d[1] for d in sorted_data]

#create a new figure with a specific size
fig = plt.figure(figsize=(20, 10))

#create the bar graph
ax = plt.subplot()
ax.bar(digraphs, occurrences, color='b')
ax.set_xlabel('Digraph')
ax.set_ylabel('Occurrences', color='b')

#set the locations and labels of the x-axis ticks
ax.set_xticks(range(len(digraphs)))
ax.set_xticklabels(digraphs)

#rotate the x-axis labels to make them vertical
plt.xticks(rotation=90)

#add padding between the subplot and the figure
plt.subplots_adjust(bottom=0.15, top=0.9)

#show the plot
plt.show()

