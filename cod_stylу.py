my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#print(type(my_list))
a = 0
#print(type(a))
#my_list = [my_list + a]
#print(my_list)
#print(len(int(my_list)))
#print(my_list)
#for i in range(12)
while  a < len(my_list) :
    if my_list[a] < 0:
        break
    if my_list[a] > 0:
        print(my_list[a])
    a += 1
