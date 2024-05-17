'''#sort lists
eng=["a","c","d","b"]
eng.sort()
print(eng)
num=[4,5,6,2,1,3]
num.sort()
print(num)

#reverse list
num=[3,4,5,65,1]
num.sort(reverse = True)
print(num)
 
num=[3,4,2,1]
num.reverse()
print(num)
num=[3,4,2,1]
num.sort(reverse=True)
print(num)

#copy a list

list=["baizid","mohammad","shikh"]
list2= list.copy()
print(list2)

list=[1,2,3,4,5,6]
list2=list

#join two list 

num1=[1,2,3,4]
num2=[5,6,7,8]
num3=num1+num2
print(num3)

num1=[1,2,3,4]
num2=[5,6,7,8]
num1.extend(num2)
print(num1)'''

a=["rahim","karim","shamim"]
b=["ratul","raisul"]
a.extend(b)
print(a)

