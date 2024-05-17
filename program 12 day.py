'''#update tuple
thisTupple=("baizid","shimul","karim","arnob")
y= list(thisTupple)
y.append("hablu")

thisTupple=tuple(y)

print(thisTupple)


fuck=(1,2,3,4,5)
love=list(fuck)
love[1]=60
fuck=tuple(love)
print(fuck)

#unpack tuple
thisTupple=("baizid","shimul","karim","arnob")
(*a,b)=thisTupple
print(a)

#loop tuple

actors=("pori moni","safa kabir","purnima","apu",)
for i in actors:
    print(i)

#range 

actors=("pori moni","safa kabir","purnima","apu",)
for i in range(len(actors)):
    print(actors[i])


#while loop

actors=("pori moni","safa kabir","purnima","apu",)
i=0
while i<len(actors):
    print(actors[i])
    i+=1

number=(1,2,3,4,5,6,7)
i=1
while i< len(number):
    print(number[i])
    i+=2
#join tuple
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
tuple3=(tuple1+tuple2)
print(tuple3)

#multiply tuple

name=("mango","banana","potoa","suger")
mesu=name*2
print(mesu)

num=(1,2,3,4,5)
mlty=num*3
print(mlty)

#tuple method
ban=(1,2,3,4,5,4,5,4,6,)
some=ban.count(4)
print(some)

data=(1,2,1,3,1,4,5,1,6,1,1)
ban=data.count(1)
print(ban)

data=(1,2,3,4,5,6,7,8,9,10)
ban=data.index(8)
print(ban)

# exercise

fruits=("apple","banana","charry")
print(fruits[0])

fruits=("apple","banana","charry")
print(len(fruits))'''

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
print(fruits.update(more_fruits))
















