## Creating a string

# s = 'this is my string'
# print(s)
# s = "this is my string"
# print(s)
# s = '''this is my string'''
# print(s)
# s = """this is my string"""
# print(s)


a = 10
b = 20
c = a + b
print(c)

"Addition of 10 and 20 = 30"


#Using + Operator :

res = "Addition of "+str(a)+" and "+str(b)+" = "+str(c)
print(res)


#Using modulus % Operation
#Format Specifiers : %d, %f, %s, %x


res = "Addition of %d and %d = %d"%(a,b,c)
print(res)


#Using format() Method

res = "Addition of {} and {} = {}".format(a,b,c, 100)
print(res)

res = "Addition of {2} and {0} = {1}".format(b,c,a, 100)
print(res)


#Using f-string

res = f"Addition of {a} and {b} = {c}"
print(res)


