#1
word = str(input("Enter your word or sentence: "))
print(word[::-1])

#2
list = ['pepsi','coke', 'sprite', 'pepsi','sprite']
def lists(list):
    print(list)
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    print(newlist)
lists(list)

#3
list1 = [1, 1, 2, 2, 3, 3, 3, 4]
list2 = [1, 2, 3, 4, 4, 5, 2, 1,]
print (list1)
print (list2)

def triples(list):
    n = False
    for i in list:
        index = list.index (i)
        if index <= len(list) -2:
             if i == list[index + 1] == list[index + 2]:
                 n = True
    print (n)
triples(list1)
triples(list2)
#4
import os
file = open(r"c:\Users\iCan Student\Desktop\myfile.txt")
lines = 0
for line in file:
    if line.strip():
        lines += 1
print (lines)

