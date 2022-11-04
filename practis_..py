file =open('myfile.txt','r')
count=0
for line in file :
    word=line.split(' ')
    count+=len(word)

file.close()
print('number of words in a text file ',count)