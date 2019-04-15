#Read an integer .
#Without using any string methods, try to print the following:
#Note that "" represents the values in between.
#Sample Input 0
#3
#Sample Output 0
#123


n = int(input("enter an integer:"))
for i in range(n):
    print(i+1,end="")
