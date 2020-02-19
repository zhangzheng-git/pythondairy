import time
print("hello")
str = "zhangzheng"
str.replace("zh","ppp")
print(str.replace("zh","ppp"))

print(str)

lin = 'a,b,c,d'
print(lin.split(','))
print(lin)

print("{} today {}".format(time.time(),time.asctime()))
print(dir(lin))
print(type(lin))
print(help(lin.split))

messge = """zjagn
zjmgt '''ninio
koaf"""
print(messge)



ju=[[1,2,3],
    [4,5,6],
    [7,8,9]]

print(ju[1])
print(ju[1][0])

print([row[1] for row in ju])

dirc = {'oodf':'zdg','wej':2,'ieng':90,'a':2,'v':9}
print(dirc)

keys1 = list(dirc.keys())
print(keys1)

keys1.sort()
for key in keys1:
    print(key,"=>",dirc[key])

# for key in sorted(dirc):
#     print(key,"=>",dir[key])

import numpy
import numpy as np
a = np.array([1,2,3])
print (a)

#下面两种等价，第二中执行效率更快
arr= []
for i in [1,2,3,4]:
    arr.append(i**i)
    print(arr)

arr = [i**i for i in [1,2,3,4]]
print(arr)



