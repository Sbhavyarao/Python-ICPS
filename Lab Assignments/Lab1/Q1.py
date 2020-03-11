def number_of_posibilities(list1):
    sub = []
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub1 = list1[i:j]  # taking sub list from mail list through iteration
            if sub1 not in sub and sub1 != []:   # checking for duplicates
                sub.append(sub1)
    return sub


N = input("enter list of integers")   # taking input from user
list1 = N.split(',')
print(number_of_posibilities(list1))   # printing output string