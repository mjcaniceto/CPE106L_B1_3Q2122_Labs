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


f = open(fileName, 'r')                     # Open the file in read mode
# Input the text, convert it to numbers, and
# add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

# Sort the list and print the number at its midpoint
numbers.sort()
midpoint = len(numbers) // 2
print("The median is", end=" ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)


f = open(fileName, 'r')                     # Open the file in read mode
# Input the text, convert its to words to uppercase, and
# add the words to a list
words = []
for line in f:
    wordsInLine = line.split()
    for word in wordsInLine:
        words.append(word.upper())

# Obtain the set of unique words and their
# frequencies, saving these associations in
# a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already seen, increment its number
        theDictionary[word] = number + 1

# Find the mode by obtaining the maximum value
# in the dictionary and determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break