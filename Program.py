import os

# Get script directory path
mypath = os.path.dirname(os.path.realpath(__file__))
# Get all files in mypath
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

print(onlyfiles)

print('Enter a line to search: ')
t = str(input(''))
with open('sampletext.txt', 'r') as txt:
    for line in txt:
        line = line.strip()
        if t in line:
            print(line)
