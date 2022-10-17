
import random
from textwrap import indent


def randomize(min,max,anz_num):
    numbers = []
    for i in range(max+1):
        numbers.append(i)
    for k in numbers:
        rand = random.randint(min,max)
        numbers[k], numbers[rand] = numbers[rand], numbers[k]
    #print(numbers[0:5])
    return numbers[0:anz_num-1]

def ziehungen(anzZiehung, min,max,anz_num):
    dic = {}
    for j in range(max+1):
            ap = {j : 0}
            dic.update(ap)
    for i in range(anzZiehung):
        num = randomize(min,max,anz_num)
        for l in num:
            a = dic.get(l) + 1
            dic.update({l: a})
        print(dic)
    return dic


#num = randomize()
ziehungen(1000,0,44,6)
#test git