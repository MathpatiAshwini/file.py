file =open("b.txt",'w')
for i in range (65,91):
    k=chr(i)
    file.write(k)
    file.write(' ')

file .close()