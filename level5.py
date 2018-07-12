import pickle
file = open('banner.p','rb')
str = pickle.load(file)
print(str)
print ('\n'.join([''.join([p[0] * p[1] for p in row]) for row in str]))
# channel