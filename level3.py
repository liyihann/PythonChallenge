import re
with open('level3.txt', encoding='utf-8') as f:
    str = f.read()

# pattern = re.compile(r'([A-Z]+)([A-Z]+)([A-Z]+)')
# m=pattern.match(str)
# print(m.group(0))
target = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',str)
for i in target:
    print(i,end="")
# linkedlist