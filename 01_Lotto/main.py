
import random


def randomize():
    numbers = []
    for i in range(45):
        numbers.append(i)
    for k in numbers:
        swapPositions(numbers, k, random.randint(0,44))
    return numbers

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def ziehungen(numbers, anzZiehung):
    dic = {}
    for j in range(45):
            ap = {j : 0}
            dic.update(ap)
    for i in range(anzZiehung):
        for l in numbers:
            a = dic.get(l) + 1
            dic.update({l: a})
        print(dic)
    return dic


num = randomize()
ziehungen(num,1000)

    