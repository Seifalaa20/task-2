for row_S in range(18):
    for col_S in range(17):
        if (col_S == 0 or col_S == 2 or col_S ==1 or col_S==3) and(row_S== 5 or row_S==6 or row_S==3 or row_S==4) or (row_S == 0 or row_S==1 or row_S==2 or row_S ==7 or row_S== 8 or row_S ==9 or row_S==14 or row_S==15 or row_S ==16) or ((col_S== 16 or col_S== 13 or col_S== 14 or col_S ==15) and (row_S == 10 or row_S == 11 or row_S== 12 or row_S ==13)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("------------------------------------------------------------------------------------------------")

for row_e in range(15):
    for col_e in range(17):
        if col_e >= 0 and col_e <=3  or ((row_e >= 0 and row_e <= 2 or row_e >= 6 and row_e <= 8 or row_e >=12 and row_e<=15) and (col_e > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print("------------------------------------------------------------------------------------------------")

for row_I in range(15):
    for col_I in range(17):
        if col_I >= 6 and col_I <=10  or ((row_I >= 0 and row_I <= 2 or row_I >=12 and row_I<=15) and (col_I > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print("------------------------------------------------------------------------------------------------")

for row_F in range(15):
    for col_F in range(17):
        if col_F >= 0 and col_F <=3  or ((row_F >= 0 and row_F <= 2 or row_F >= 6 and row_F <= 8) and (col_F > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print("------------------------------------------------------------------------------------------------")
