a=['playing','singing','cooking','cook','going','choclate','starting','footboll']


file=open('a.txt','w')
i=0
while i<len(a):
    if 'ing'  in a[i]:
        file.write(a[i])
        file.write('\n')

    i+=1
file.close()

