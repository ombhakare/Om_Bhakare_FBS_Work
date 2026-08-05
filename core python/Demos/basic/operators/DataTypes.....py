###Numeric

# 1. int
x = 10
print(type(x))

# 2. float
x = 3.14
print(type(x))
 
# 3. complex

x = 10 + 5j #Real + imaginary
print(type(x))


#### Text
#str (string)
x = 'first bit solution'
x = "first bit solution's"
x = """this is first line
this is second line
this is third line"""
print(type(x))


###  Sequentials
# 1. list
x = [1,2,'abc',3.14]
print(type(x))

# 2. tuple
x = (1, 2, 'abc',3.14)
print(type(x))

# 3. range
x = range(1,20)
print(type(x))


#### Set type
## 1. set
x = {1,2,'abc',3.14}
print(type(x))

## 2. frozenset
x = frozenset({1,2,'abc', 3.14})
print(x)
print(type(x))


#### Mapping
# 1. dict (dictionary)
x = {'name':"om bhakare", 'dept':'training'}


#### Boolean
#1. True
x = True

#2. false
x = False

#### None type
x = None
print(x)
print(type(x))