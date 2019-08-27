myList=[]
for i in range(200):
        myList.append(i+1)

print(myList[3])

myList.append(int(input("1st number: ")))
myList.append(int(input("2nd number: ")))
myList.append(int(input("3th number: ")))
myList.append(int(input("4th number: ")))
print("4th number is %d" % myList[-1])
print("3th number is %d" % myList[-2])