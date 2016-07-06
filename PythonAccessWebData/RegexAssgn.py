# Searching numbers in a HayStack
import re
try:
    fhandle = open("regex_sum_279055.txt")
except:
    print("Input File not found")
    exit()

sum = 0
for line in fhandle:
    numbers = re.findall("([0-9]+)", line)
    for number in numbers:
        sum += int(number)
print(sum)
