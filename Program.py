with open ('sampletext.txt','r') as txt:
    for line in txt:
        line = line.strip()
        print(line)
