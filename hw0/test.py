import collections


file=open("word.txt",'r')

dict={}

list=[]


for line in file.readlines():
    words=line.split()
    for word in words:
        if dict.__contains__(word):
            dict[word]+=1
        else:
            dict[word]=1
            list.append(word)

i=0;
for word in list:
    print(word,i,dict[word])
    i+=1


        
