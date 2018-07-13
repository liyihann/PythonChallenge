import zipfile
import re

file = zipfile.ZipFile("channel.zip","r")
for name in file.namelist():
    print(name)

print(file.open("readme.txt").read().decode('utf-8'))
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip
comments=[]
def nextFile(name):
    path = name+".txt"
    str = file.open(path).read().decode('utf-8')
    try:
        newName = re.search(r'([0-9]+)', str).group(1)
        comments.append(file.getinfo(path).comment.decode('utf-8'))
        return newName
    except:
        print(str)
        return ''
p = '90052'
for i in range(1,len(file.namelist())):
    print('{}:{}'.format(i,p))
    p = nextFile(p)
print("".join(comments))

file.close()