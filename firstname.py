FirstNameList=[]
len=int(input("How many names do you want to insert"))
for i in range(0,len):
    fname=input("enter first name you want to add list")
    FirstNameList.append(fname)
    count_a=0
for names in FirstNameList:
    count_a+=names.count("a")
print(count_a)
