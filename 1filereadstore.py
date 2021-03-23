l=[]
f=open("demo.txt","w")
n=int(input("enter number of lines:"))
for i in range(n):
    f.write(input("enter text here:")+"\n")
f.close()
f=open("demo.txt","r")
for i in f:
    l.append(i[:-1])
f.close()
print(l)