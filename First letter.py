for row in range(18):
    for col in range(17):
        if (col == 0 or col == 2 or col ==1 or col==3) and(row== 5 or row==6 or row==3 or row==4) or (row == 0 or row==1 or row==2 or row ==7 or row== 8 or row ==9 or row==14 or row==15 or row ==16) or ((col== 16 or col== 13 or col== 14 or col ==15) and (row == 10 or row == 11 or row== 12 or row ==13)):
            print("*",end="")
        else:
            print(end=" ")
    print(end="\n")