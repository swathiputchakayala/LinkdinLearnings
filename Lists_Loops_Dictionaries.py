#Lists
a = [1,'sugar',5,7,9]
b = [True, False]
c = [1.02, 48.054, 46.48]
print(a)
print(b[0])

d = ["apple","babana"]
d.append("carrot")# appends helps in adding the avle to the list
print(d)

e = len(a) # given the lenght of the list a. So ans will be 5
print(e)

f = [1,2,3,4,5,6]
f.insert(0,"Inserted Value")#put the value in specific place
print(f)

g = [4,5,6,7,8,9,10]
del(g[4]) # delets the value at the index = 4
print(g)

#LOOPS
for number in range(10):
     print(number*2)
     
for num in range(len(g)):
    print(g[num])
    
# Dictionaries
'''
They are called as key-value pair.
We use {key : value} for it.
'''
cats = {"tom":20, "Jane":6}
cats["Jimmy"] = 1 # adding Jimmy to Dictionary
print(cats)


## example test
temp = 0
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        temp = temp + numbers[i]
    else:
        pass
print(temp)