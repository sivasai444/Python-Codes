char=input("entre the characret to be printed:")
num_rows=int(input("no.of rows:"))
for i in range(1,num_rows+1):
    for j in range(1,i+1):
        print(char,end="")
        print()
