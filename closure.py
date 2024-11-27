
def greet(name):
    print(name)

    def display_name():
        print(name)

    return display_name

spam = greet('Jimmy')
print(type(spam))




def multiply(multiplier):
    return lambda x: x * multiplier

doubler = multiply(2) # now doubler contains mutliply function with 2 already passed in as mutlipler
trippler = multiply(3)

print(doubler(10)) # now because above the 2 is in scope for ther inner fucntion or lambda. it now is returning the inner functiuon and the value passed in is 10 but it also remembers mutlpioer as 2
print(trippler(5))#same as above except it remembers mutiuplier as 3 .... 

