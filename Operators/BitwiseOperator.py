Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=60
>>> b =13
>>> print("a=",a ,':',bin(a),'b=',b,':',bin(b))
a= 60 : 0b111100 b= 13 : 0b1101
>>> c=0
>>> c=a&b;
>>> print("result of AND is ",c,':',bin(c))
result of AND is  12 : 0b1100
>>> c=a | b
>>> print("Result of OR is ",c,':',bin(c))
Result of OR is  61 : 0b111101
>>> c = a ^ b
>>> print("Result of EXOR is",c ,':',bin(c))
Result of EXOR is 49 : 0b110001
>>> c = ~a;
>>> print("Result of COMPLEMENT is ",c, ':',bin(c))
Result of COMPLEMENT is  -61 : -0b111101
>>> c = a <<2
>>> print("Result of LEFT SHIFT is", c ,':',bin(c))
Result of LEFT SHIFT is 240 : 0b11110000
>>> c = a >> 2;
>>> print("Result of RIGHT SHIFT" ,c ,':',bin(c))
Result of RIGHT SHIFT 15 : 0b1111
