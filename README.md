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
