for i in [5,4,3,2,1]:
    print(i)


largest_so_far = -1
print('Before', largest_so_far)
for the_num in [3,5,2,67,43,67,85,43]:
    if the_num > largest_so_far:
        largest_so_far = the_num

print('After',largest_so_far)