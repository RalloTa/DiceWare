import random,threading
words=[]
test=[]
word=open('20k.txt','r')

passwd=''
for x in range(6):
    passwd=passwd+(words[random.randint(0,len(words))])
print(passwd)
