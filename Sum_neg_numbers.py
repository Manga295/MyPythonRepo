given_list =[5,4,3,2,1,-1,-4,-5,-6]
total =0
j=len(given_list) -1
while  True :
    if given_list[j] < 0:
        total+= given_list[j]
        j -= 1
print(total)


