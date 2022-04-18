"""
File: mean.py
Prints the mean/average of a set of numbers in a file.
"""

fileName = input("Enter the file name: ")   
f = open(fileName, 'r')        

# Input the text, convert it to numbers, and
# add the numbers to a list

sum=0                               # reseting sum to 0
n=0                                 # reseting number of data to 0

for line in f:                          # For each line in file (read)
    sum+=float(line.strip())            # Add each number to have sum
    n+=1                                # Increment by 1 until nothing to add
print ('The mean is:', (sum/n))         # Outputs the mean/average