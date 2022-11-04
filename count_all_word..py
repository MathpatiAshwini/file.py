file=open("my_file..txt","r")
c=file.read()
a=c.split()
count=0
i=0
while i<len(a):
    count+=1
    i+=1
print(count)
file.close()