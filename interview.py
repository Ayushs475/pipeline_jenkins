'''def inner(name):
    if name=='sunny':
        print("hello",'sunny',"BadMorning")
    else:
         wish(name)
         return inner

@decorator
def wish(name):
    print("hello",name,"Good morning")
wish("Durga")
wish("ravi")
wish("sunny")'''


def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greetings=func(""" hi I am ayush """)
    print(greetings)

greet(shout)
greet(whisper)

'''
l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    print(i)


syntax:copy.deepcopy()
syntax:copy.copy()

import copy

deep=[1,2,[3,5],4]    # shallow copy 
deep1=copy.copy(deep)
print("deep1 ID",id(deep1),'value',deep1)

deep2=copy.deepcopy(deep)    # deep copy
print("deep2 ID",id(deep2),'value',deep2)'''