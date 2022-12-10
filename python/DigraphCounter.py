# Import the multiprocessing module
import multiprocessing

import concurrent

# Import the ProcessPoolExecutor class from the concurrent.futures module
from concurrent.futures import ProcessPoolExecutor

# Import time to be able to use the timer
import time

# Add the following lines of code at the top of your program, before importing any other modules
# This tells the multiprocessing module to use an alternative process creation method that is supported on Windows
if __name__ == '__main__':
    multiprocessing.freeze_support()
    
# Import the Counter class from the collections module
from collections import Counter

# Import CSV to be able to use csv functions
import csv
# Import the sys module to access command-line arguments
import sys

# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Access the filename passed by the third program
filename = sys.argv[1]

file_path1 = os.path.join(cwd, "./resources", 'digraphs.txt')
file_path2 = os.path.join(cwd, "./csv", 'digraphcount.csv')

# Open the file containing the list of digraphs and read the contents into a string
with open(file_path1, 'r') as f:
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
        # Split the input string into chunks
        chunk_size = len(input_string) // multiprocessing.cpu_count()
        chunks = [input_string[i:i+chunk_size] for i in range(0, len(input_string), chunk_size)]

        # Create a Counter object to store the counts of each digraph
        digraph_counts = Counter()

        # Check if the code is running in the main module
        if __name__ == '__main__':
            # Create a ProcessPoolExecutor
            with concurrent.futures.ProcessPoolExecutor() as executor:
                # Distribute the work of counting the occurrences of each digraph in the chunks
                future_to_chunk = {executor.submit(self._count_chunk, chunk): chunk for chunk in chunks}
                for future in concurrent.futures.as_completed(future_to_chunk):
                    chunk = future_to_chunk[future]
                    try:
                        # Aggregate the partial results into a single Counter
                        partial_result = future.result()
                        digraph_counts.update(partial_result)
                    except Exception as exc:
                        print('%r generated an exception: %s' % (chunk, exc))

        # Return the Counter of digraph counts
        return digraph_counts

    def _count_chunk(self, chunk):
        # Start the chunk timer
        start_time = time.perf_counter()
        # Create a Counter object to store the counts of each digraph in the chunk
        digraph_counts = Counter()

        # Iterate through each character in the chunk
        for i, char in enumerate(chunk):
            # Check if the previous character forms a digraph with the current character
            if i > 0:
                prev_char = chunk[i-1]
                digraph = Digraph(prev_char, char)
                if digraph in self.digraphs:
                    # If the digraph exists in the list, increment its count in the Counter
                    digraph_counts[digraph] += 1
        # Stop the timer and calculate the elapsed time
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
        # Print the elapsed time and the size of the chunk
        print("Chunk took %fms to complete %dkb\n" % (elapsed_time * 1000, len(chunk) / 1024))

        # Return the Counter of digraph counts for the chunk
        return digraph_counts

# Create instances of the Digraph class for each digraph in the list
digraph_objects = [Digraph(d[1], d[3]) for d in digraph_list]

# Create an instance of the DigraphCounter class and pass it the list of digraph objects
digraph_counter = DigraphCounter(digraph_objects)

# Open the file and create a CSV writer
with open(file_path2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Digraph', 'Count'])

    # Count the occurrences of each digraph in the input string
    # Open the file and read the contents into a string
    with open(filename, 'r') as f:
        input_string = f.read()
    digraph_counts = digraph_counter.count(input_string)

    # Print the counts of each digraph
    for digraph, count in digraph_counts.items():
        print(f"{digraph.first}{digraph.second}: {count}")

    # Write a row for each digraph and its count
    for digraph, count in digraph_counts.items():
        writer.writerow([f"{digraph.first}{digraph.second}", count])