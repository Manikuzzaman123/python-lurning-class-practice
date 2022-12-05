

def Sum_Two_Index_Number_Inside_TheList(list,target):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j] == target:
                return([i,j])
list=[1,2,3,4,56,7,8,9,10,11,12,13,14,15,16,17,18,19]

target=15

print(Sum_Two_Index_Number_Inside_TheList(list,target))