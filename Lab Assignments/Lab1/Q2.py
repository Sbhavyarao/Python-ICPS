import operator


def concatenateDic(di1, di2):
    di2.update(di1)
    sorted_d = sorted(di2.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_d)
    #print(sorted(di2.items(), key=lambda k (k[1], k[0])))


if __name__ == '__main__':
    di1 = dict({'Bhavya': 25, 'Ravi': 22, 'Mani': 26, 'Jhon': 20})
    di2 = {'a': 27, 'b': 24, 'M': 29, 'J': 19}
    sorted_dict = {}
    concatenateDic(di1, di2)
