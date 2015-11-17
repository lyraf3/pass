t = str(input(''))
with open ('sampletext.txt','r') as txt:
    for line in txt:
        line = line.strip()
        if t in line:
            print(line)
