testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
new_testlist = {}
for i in testList:
    if type(i) == set:
        new_testlist.update(i)
    elif type(i) == list:
        new_testlist.update(i)
print(True)
print(new_testlist)