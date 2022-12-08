#Import CSV to be able to use csv functions
import csv

# Open the file containing the list of digraphs and read the contents into a string
with open('digraphs.txt', 'r') as f:
    digraph_string = f.read()

# Split the string into a list of individual digraphs
digraph_list = digraph_string.split()

# Define the Digraph class
class Digraph:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        # Check if the first and second characters of the other object are the same as the current object
        if other is None:
            return False
        return self.first == other.first and self.second == other.second

    # Add the __hash__ method so that Digraph objects can be used as keys in a dictionary
    def __hash__(self):
        return hash(self.first) ^ hash(self.second)

# Define the DigraphCounter class
class DigraphCounter:
    def __init__(self, digraphs):
        self.digraphs = digraphs

    def count(self, input_string):
        # Create a dictionary to store the counts of each digraph
        digraph_counts = {}

        # Iterate through each character in the input string
        for i, char in enumerate(input_string):
            # Check if the previous character forms a digraph with the current character
            if i > 0:
                prev_char = input_string[i-1]
                digraph = Digraph(prev_char, char)
                if digraph in self.digraphs:
                    # If the digraph exists in the list, increment its count in the dictionary
                    if digraph in digraph_counts:
                        digraph_counts[digraph] += 1
                    else:
                        digraph_counts[digraph] = 1

        # Return the dictionary of digraph counts
        return digraph_counts

# Create instances of the Digraph class for each digraph in the list
digraph_objects = [Digraph(d[1], d[3]) for d in digraph_list]

# Create an instance of the DigraphCounter class and pass it the list of digraph objects
digraph_counter = DigraphCounter(digraph_objects)

# Open the file and create a CSV writer
with open('digraphcount.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Digraph', 'Count'])

    # Count the occurrences of each digraph in the input string
    # Open the file and read the contents into a string
    with open('teest.txt', 'r') as f:
        input_string = f.read()
    digraph_counts = digraph_counter.count(input_string)

    # Print the counts of each digraph
    for digraph, count in digraph_counts.items():
        print(f"{digraph.first}{digraph.second}: {count}")

    # Write a row for each digraph and its count
    for digraph, count in digraph_counts.items():
        writer.writerow([f"{digraph.first}{digraph.second}", count])
