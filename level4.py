import urllib
import re
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
# peak.html