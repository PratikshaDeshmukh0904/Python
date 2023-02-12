a=20
b=a
print("a",a,"b",b)

if(id(a) == id(b)):
    print("a and b have same identity")
else:
    print("a and b have not same identity")
    
