'''Use range() to print numbers from 0 to 49 in 5 aligned rows of 10 numbers each (0–9 on row 1, 10–19 on row 2, etc.).
'''
for i in range(0,50):
    if i%10 ==0:
        print("")
    print(i,end=" ")