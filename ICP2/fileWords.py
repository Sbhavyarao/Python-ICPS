infile = open('abc.txt', 'r')
inputline = infile.readline()
outputDict = {}
while inputline != "":
    for s in inputline.split():
        if s in outputDict:
            i = outputDict[s]
            outputDict[s] += i
        else:
            outputDict[s] = 1
    inputline = infile.readline()
print(outputDict)
