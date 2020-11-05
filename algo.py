# Time COMPLEXITY
# Time complexity is O(n) - linear algorithm,
# As we have one loop to go through all chars in string.

# SPACE COMPLEXITY
# Space complexity is O(n)

inputList = []
outputList = []

# Read input from the file
file1 = 'input.txt'
with open(file1) as f_obj:
    for line in f_obj:
        inputList.append(line.rstrip())


# Function for converting strings and adding them to output list of Strings
def convert_string(string):
    length = len(string)
    count = 1
    result = []
    i = 0
    for i in range(0, length - 1):
        if string[i] == string[i + 1]:
            count += 1
            i += 1
        else:
            result.append(string[i])
            result.append(str(count))
            count = 1
            i += 1
    result.append(string[length - 1])
    result.append(str(count))
    outputList.append("".join(str(x) for x in result))


# Function call for converting inputList if the list is not empty
if inputList:
    for element in inputList:
        convert_string(element)


# Writing output to the text file
file2 = 'output.txt'
with open(file2, 'w') as f:
    for element in outputList:
        f.write(element + "\n")
