import subprocess

# Hard-coded filename to pass to the other programs
filename = 'teest.txt'

# Launch the first program, CharCounter.py, and pass the filename as an argument
p1 = subprocess.run(['python', 'CharCounter.py', filename])

# Check the exit code of the first program to ensure it ran successfully
if p1.returncode == 0:
    # Launch the second program, DigraphCounter.py, and pass the filename as an argument
    p2 = subprocess.run(['python', 'DigraphCounter.py', filename])

    # Check the exit code of the second program to ensure it ran successfully
    if p2.returncode == 0:
        print('Both programs ran successfully!')
    else:
        print('Error: The second program failed to run')
else:
    print('Error: The first program failed to run')