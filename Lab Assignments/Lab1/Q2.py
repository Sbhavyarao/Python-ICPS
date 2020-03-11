import operator


def Merge(dist1, dist2):
    return {**dist1, **dist2}   # Merging two dictionaries by using '**kwargs'


Dist1 = {"Mani": 92, "Nani": 85, "pane": 78, "hhr": 65}
Dist2 = {'d': 45, 'r': 67, 'y': 56, 'T': 87, 'h': 34}
Dist3 = Merge(Dist1, Dist2)
print("Merged Dictionary: ", Dist3)
sorted_d = sorted(Dist3.items(), key=operator.itemgetter(1))  # sorting dictionary by using sorted method
Dist4 = dict(sorted_d)
print("Sorted Dictionary: ", Dist4)