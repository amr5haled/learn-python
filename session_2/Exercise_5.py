'''Ask the user for three integers: lower limit, higher limit, and step. Use range() to print numbers from low to high (inclusive) with that step.'''
lower_num=int(input("Enter an integer number for lower limit: " ))
higher_num=int(input("Enter an integer number for higher limit: " ))
st_ep=int(input("Enter an integer number for step: " ))
for i in range(lower_num,higher_num+1,st_ep):
    print(i)
    