file=open('myfile.txt','r')
long=''
for line in file:
    if len(line)>len(long):
        long=line
print(long)