

list = [1, 2, 3, 7, 11, 15, 22, 41, 33, 21, 10, 78, 30, 80, 44, 64, 50,15]
lst_len = len(list)
target = 3
for x in range(0,len(list)):
    for y in range(x+1,len(list)):
        if x+y == target:
            print([x,y])
