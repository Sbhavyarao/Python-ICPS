def string_alternative():
    inputString = input('Enter the input: ')
    outputString =''
    for i in range(len(inputString)):
        if i%2 == 0:
            outputString += inputString[i]
    print(outputString)
if __name__ == '__main__':
    string_alternative()

