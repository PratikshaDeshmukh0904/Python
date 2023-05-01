# anonimius function is also called lambda function
# the function which define without using def keyword and function name
#using def keyword
'''
def add():
    a=20
    b=30
    return a+b
print(add())
'''
#using lambda function
#right hand side operation
#left hand side declaration

add = lambda a = 20 ,b = 30:a + b
print(add())

sub=lambda a,b:a+b
print(sub(50,30))
print(type(sub))
print(sub)



demo = lambda a,b:a+b
x=int(input())
y=int(input())
print("addition is",demo(x,y))

'''
power =lambda a,b:pow(a,b)
print(power(3,4))
'''
power =lambda a,b:a**b
print("Power is",power(3,4))

square =lambda a:a*a
print("Square is",square(4))
