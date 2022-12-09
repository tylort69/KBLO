import subprocess

# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

temp = os.path.join(cwd, "./resources", "demofile.txt")

# Hard-coded filename to pass to the other programs
filename = temp

# Launch the first program, CharCounter.py, and pass the filename as an argument
p1 = subprocess.Popen(['python', 'CharCounter.py', filename])

# Launch the second program, DigraphCounter.py, and pass the filename as an argument
p2 = subprocess.Popen(['python', 'DigraphCounter.py', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Use the communicate method to read the output of the second subprocess as it's being generated
output, error = p2.communicate()

# Print the output of the second subprocess
print(output)

# Wait for both programs to finish
p1.wait()
p2.wait()

# Check the exit codes of both programs to ensure they ran successfully
if p1.returncode == 0 and p2.returncode == 0:
    print('Both programs ran successfully!')
else:
    print('Error: One or both of the programs failed to run')
