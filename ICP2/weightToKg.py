N = input('enter number of students: ')
li = []
while len(li) < int(N):
    li.append(int(input('enter student weights: ')))
for i in range(len(li)):
    li[i] = round((li[i]/2.22),2)
print(li)
#ouput = [round((a/2.22),2) for a in li]
#print(ouput)