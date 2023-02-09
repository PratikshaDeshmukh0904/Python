a=10
b=20
list = [1,2,3,4,5]
print(list)
print("a=",a,"b=",b)
if(a in list):
    print("Line 1 - a is available in the given list")
else:
    print(" a is not available")
    
if( b not in list):
    print("b is not available in the given list")
else:
    print("b is available in the given list")
