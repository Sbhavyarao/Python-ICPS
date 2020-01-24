# inputString = list(input())
# print(inputString)
# print('enter indexes you wish to remove')
# index = list(input())
# print(index)
# for i in range(len(index)):
#     inputString.pop(i)
# inputstr=''.join(inputString)
# print(inputstr[::-1])
# print(inputstr)

inputString = input()
ShortInput = inputString[:len(inputString)-2]
print(ShortInput[::-1])
