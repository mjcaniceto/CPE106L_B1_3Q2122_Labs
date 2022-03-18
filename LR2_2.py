filename = input('Enter the file name: ')
NumLines = []
with open(filename, 'r') as f:
    for line in f:
        NumLines.append(line.strip())

while True:
    print("The file has", len(NumLines), "lines. Enter 0 if you want to quit the program")
    if len(NumLines) == 0:
        break
    lineNumber = int(input("Enter a line number: "))
    if lineNumber == 0:
        break
    elif lineNumber > len(NumLines):
        print("ERROR: line number must be less than or equal to", len(NumLines))
    else:
        print("Line number",lineNumber, ":", NumLines[lineNumber - 1])