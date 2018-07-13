# PythonChallenge
My solutions for http://www.pythonchallenge.com/
## Level 0
Hint: try to change the URL address.  
http://www.pythonchallenge.com/pc/def/0.html  
将url改为1.html,提示：``2**38 is much much larger``.  
计算``2**38``:  

```python
print(2**38)
```
输出结果为``274877906944``  
得到Level 1地址：  
http://www.pythonchallenge.com/pc/def/274877906944.html
## Level 1
图片提示：``K->M``,``O->Q``,``E->G``  
hint：  
```
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
```
可以猜出该题使用的是恺撒密码，各字母向后位移2位  

```python
intab =  'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = str.maketrans(intab,outtab)
str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
print(str.translate(trantab))
```
输出结果为：  
```
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and thats why this text is so long. using string.maketrans() is recommended. now apply on the url.
```
根据提示，要对url进行转换，现在的url为``map.html``  

```python
str2 = 'map'
print(str2.translate(trantab))
```
输出结果为``ocr``  
得到Level 2地址：  
http://www.pythonchallenge.com/pc/def/ocr.html
## Level 2
hint:``recognize the characters. maybe they are in the book, 
but MAYBE they are in the page source.``  
打开页面源码，发现注释中有大量字符，有这样的提示：  
``find rare characters in the mess below``  
把该部分注释复制到txt文件中以便读取：[level2.txt](./level2.txt)  
要在大量乱码字符中找到英文字母  

```python
with open('level2.txt', encoding='utf-8') as f:
    str = f.read()
target=''
for ch in str:
  if ch.isalpha():
    target+=ch
print(target)
```
输出结果为``equality``  
得到Level 3地址：  
http://www.pythonchallenge.com/pc/def/equality.html
## Level 3
hint:  
``One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.``  
打开网页源码，发现注释中有大量大小写英文字母字符  
把该部分注释复制到txt文件中以便读取：[level3.txt](./level3.txt)    
结合提示，猜想需要找到左右均有三个大写字母的小写字母 . 

```python
with open('level3.txt', encoding='utf-8') as f:
    str = f.read()
target = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',str)
for i in target:
    print(i,end="")
```
输出结果为``linkedlist``  
得到Level 4地址：  
http://www.pythonchallenge.com/pc/def/linkedlist.html  
实际需要跳转至  
http://www.pythonchallenge.com/pc/def/linkedlist.php  
## Level 4
点击图片，页面跳转，url后面增加``nothing=12345``  
页面内容为：``and the next nothing is 44827``  
结合初始页面源码注释中的：  
``urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.``  
需要借助urllib库不断爬取url中的新值，循环次数可以设为400次  

```python
def nextPage(p):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+p
    str = urllib.request.urlopen(url).read().decode('utf-8')
    try:
        newP = re.search(r'([0-9]+)', str).group(1)
        return newP
    except:
        print(str)
        return ''

p = '12345'
for i in range(1,400):
    print('{}:{}'.format(i,p))
    p = nextPage(p)
```
爬至第86次时，会出现异常情况：  
``Yes. Divide by two and keep going.``  
本来应该手动计算一下再继续爬取，后来发现直接跳过对结果也没有影响  
爬至第357次时出现``peak.html``  
得到Level 5地址：  
http://www.pythonchallenge.com/pc/def/peak.html   
## Level 5
level5的页面标题为``peak hell``,hint为``pronounce it ``  
页面注释中有：``peak hell sounds familiar ? ``  
搜索之后才知道这个需要用的是pickle库  
注释中有文件：``banner.p``，下载至本地以便读取：[banner.p](./banner.p)  
使用pickle库将文件中的字符多维数组格式化输出，转换为字符图像

```python
file = open('banner.p','rb')
str = pickle.load(file)
print(str)
print ('\n'.join([''.join([p[0] * p[1] for p in row]) for row in str]))
```
输出结果为:  
```
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
```
即``channel``  
得到Level 6地址：  
http://www.pythonchallenge.com/pc/def/channel.html  
## Level 6
页面源码注释有提示：``<-- zip -->``  
将url后缀``html``改为``zip``得到 ``channel.zip``，放入项目文件夹  
调用``zipfile``对压缩文件进行操作  
首先检查一下文件列表：  
 
```python
file = zipfile.ZipFile("channel.zip","r")
for name in file.namelist():
    print(name)
```
输出了全部文件名，发现有一个``readme.txt``文件，查看内容：  

```python
print(file.open("readme.txt").read().decode('utf-8'))
```
输出：  

```
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip
```
那么就从名字为``90052.txt``的文件开始遍历：  

```python
def nextFile(name):
    path = name+".txt"
    str = file.open(path).read().decode('utf-8')
    try:
        newName = re.search(r'([0-9]+)', str).group(1)
        return newName
    except:
        print(str)
        return ''
p = '90052'
for i in range(1,len(file.namelist())):
    print('{}:{}'.format(i,p))
    p = nextFile(p)
file.close()
```
输出了遍历过程中各文件名字之后，最后有这样的提示：``Collect the comments.``  
根据提示，需要对文件的``comment``进行操作  
以上代码修改为：  

```python
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
```
输出结果为：  

```
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
```
即``hockey``  
打开地址：  
http://www.pythonchallenge.com/pc/def/hockey.html  
提示：``it's in the air. look at the letters.``  
看来答案不是上面图像中的字母形状，改为拼成各字母形状的字母：``oxygen``  
得到Level 7地址：  
http://www.pythonchallenge.com/pc/def/oxygen.html 

