#Filter Function
lst = [67,89,8,76,41]
odd = list(filter(lambda a : a%2 !=0,lst))
print("Odd Numbers",odd)


#map Function
sqr=[2,4,6,8,10]
square =tuple( map(lambda a : a*a,sqr))
print("Square",square)


#Filter Function
marks =[55,70,72,34,80,18,52,32]
pass_student = tuple(filter(lambda m : m>35,marks) )
print("Pass Student",pass_student)


#Without Map Function
marks1 =[120.7,143.7,150.4,145.6,192.6]
x=[]
for i in marks1:
    c=i/2
    x.append(c)
print("Average",x)



#With Map Function
marks2 =[120.7,143.7,150.4,145.6,192.6]
x1=list(map(lambda m :m/2,marks2))
print("USing Map Function Calculate Average",x1)


#Reduce Function perofrm action on list
#For Reduce import library

from functools import reduce

lst1=[67,8,78,69,45,32]
add = reduce(lambda x,y:x+y ,lst1)
print("Addition",add)

#Reduce is used reduce code ,reduce return single value
#they allow to use reduce size of code and without using complexity like loops.

