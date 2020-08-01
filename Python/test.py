list1 = [1, 2, 1, 2, 3, 4, 5, 6]

for i in list1:
    frequency = list1.count(i)

    if frequency == 2 or frequency == 3:
        print(i)
