#Comment:

#1. It is used to document the code
#2. Any line of code that is commented, will not get executed by interpreter.

#=> Single line comment :
#-> It is done by using # in front of the line that you want to comment

#print('Hello Sakeeb') #This is print statement

#==> Multiline Comment :
'''
a = 10
b = 20
c = a + b
print(c)
'''

"""
a = 10
b = 20
c = a + b
print(c)
"""

#Triple quotes are used for :
#1. Multiline Commenting
#2. Creating Docstring for Method and functions.

#======================================================

#==> Fundamental DataTypes :

#Int, Float, Complex, Bool, Str

#1. Int : int()

#1) Decimal Number (0-9)

"""
a = 123456789
print(a, type(a))

#2) Binary Number (0 and 1) ==> bin()
a = 0b1001
print(a, type(a))


#3) octal Number (0-7) ==> oct()
a = 0o777
print(a, type(a))


#3) HexaDecimal Number (0-9 and A-F / a-f) ==> hex()
a = 0xf
print(a, type(a))
"""

#====================================================

#2. float ==> float()
"""
f = 10.25
print(f, type(f))
"""


#====================================================

#3. complex()
"""
a = 10+20j
print(a, type(a))

print(a.real)
print(a.imag)
"""

#====================================================

#4. bool ==> bool()
#True / False

"""
a = True
print(a, type(a))

a = False
print(a, type(a))
"""

#====================================================

#5. String ==> str()

s = 'This is my string'
#print(s, type(s))

s = "This is my string2"
#print(s, type(s))


s = '''This is my string3'''
#print(s, type(s))


s = """This is my string4"""
#print(s, type(s))



##x = '''THis is my first line
##THis is my second line
##this is my third line'''
##print(x)


##x = """THis is my first line
##THis is my second line
##this is my third line"""
##print(x)


##s = "THis is my first line\nTHis is my second line\nthis is my third line"
##print(s)


##x = """THis is my first line
##THis is my second line
##this is my third line"""
##print(x)

#=====================================================

#==> TypeCasting

#1. int()
"""
a = 10.25
x = int(a)
print(x, type(x))


##a = 10+20j
##x = int(a)  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
##print(x, type(x)) 


a = True
x = int(a)
print(x, type(x))

a = False
x = int(a)
print(x, type(x))


a = '10'
print(a, type(a))
x = int(a)
print(x, type(x))

##a = '10.25'
##x = int(a) #ValueError: invalid literal for int() with base 10: '10.25'
##print(x, type(x))


##a = 'c'
##x = int(a) #ValueError: invalid literal for int() with base 10: 'c'
##print(x, type(x))
"""
#==========================================================

#2. float()
"""
a = 10
x = float(a)
print(x, type(x))

##a = 10+20j
##x = float(a) #TypeError: float() argument must be a string or a real number, not 'complex'
##print(x, type(x))


a = True
x = float(a)
print(x, type(x))

a = False
x = float(a)
print(x, type(x))


a = '10'
x = float(a)
print(x, type(x))


a = '10.25'
x = float(a)
print(x, type(x))


##a = 'c'
##x = float(a) #ValueError: could not convert string to float: 'c'
##print(x, type(x))
"""


#======================================================

#3. bool()
##0 ==> Zero
##'' ==> Empty
##[] ==> Empty
##None

"""
a = 10
x = bool(a)
print(x, type(x))

a = -10
x = bool(a)
print(x, type(x))

a = 0
x = bool(a)
print(x, type(x))

a = 10+20j
x = bool(a)
print(x, type(x))

a = 0+0j
x = bool(a)
print(x, type(x))

a = 10.5
x = bool(a)
print(x, type(x))

a = 0.0
x = bool(a)
print(x, type(x))


a = 'abc'
x = bool(a)
print(x, type(x))

a = ''
x = bool(a)
print(x, type(x))

a = '0'
x = bool(a)
print(x, type(x))

a = None
x = bool(a)
print(x, type(x))
"""

#======================================================

#==> String ==> str()
"""
a = 10
x = str(a)
print(x, type(a), type(x))


a = 10.25
x = str(a)
print(x, type(a), type(x))


a = 10+25j
x = str(a)
print(x, type(a), type(x))


a = True
x = str(a)
print(x, type(a), type(x))


a = [1,2,3,4,5,6,7,8,9]
x = str(a)
print(x, type(a), type(x))
"""
