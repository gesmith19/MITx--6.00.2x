PATH_TO_FILE = 'julyTemps.txt' 
def loadFile():
    inFile = open(PATH_TO_FILE, 'r', 0)
    print' opened file OK'
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        print fields
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    print 'high is: ', high
    print 'low is: ', low
    return (low, high)
    
x = loadFile()