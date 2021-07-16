import csv 
import math

with open('class1.csv',newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]

def mean(meandata):

    n = len(meandata)

    total = 0

    for x in meandata:
        total = total + int(x)

    mean =  total/n
    return mean

slist = []
for number in data:
    a = int(number) - mean(data)
    a = a **2 
    slist.append(a)


b = 0

for z in slist:
    b = b + z


length = len(data)
length = length - 1

ans = b/length
standarddiv = math.sqrt(ans)

print(standarddiv)