#Functions
def bark():
    print("Woof! Woof!")
    print("u r a dog!")
bark()
for i in range(100):
    bark()

def hello():
    name = "Swathi"
    print(f"Hello {name}!")
hello()

#or

def hello(name):
    print(f"Hello {name}! Have a good day")
hello("Sravanthi")

## Adding 2 numbers
def add_numbers(num1,num2):
    print(num1 + num2)
add_numbers(2,8)

## Dog Info

def info(age,name):
    print(f"The name of the dog is {name}. Age of {name} it is {age} ")
info(10,"Tommy")

def double(number):
    return number*2
print(double(6))


def string(word):
    return(word.upper())
Uppercase = string("swathi")
print(Uppercase)


def uppercase(name):
    return(name.upper())

names = ["Swathi","Sravas","Lilly"]
for name in names:
    print(uppercase(name))
    

#input
user_text = input('Hey this is from input:')
print(user_text)

Output_string = input('Hey this is from Output_string:')
print(Output_string*2)

Number_string = input('Hey this is from Number_string:')
print(int(Number_string)*2)


##### Code challange
