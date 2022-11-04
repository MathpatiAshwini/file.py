file=open("my_file..txt","r")
c=file.read()
a=c.split()
user=input("enter the word----")
# user="my"
count=0
i=0
while i<len(a):
    if a[i]==user:
        count+=1
    i+=1
print(count)
file.close()