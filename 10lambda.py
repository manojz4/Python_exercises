def greeting ():
    return "hello"
    
# print( id(greeting()  )  )
# print(greeting)

# var = greeting
# print(var)

# Higher order function
def enhanced_greeting(greeting_function , add_greeting):
    return greeting_function() + add_greeting

print(greeting())
print(enhanced_greeting(greeting," You are  wonderful!"))

# another example Higher order 
def enhanced_greeting_1(salutation):
    
    def greeting_function():
        return "Hello " + salutation
    
    return greeting_function

# print(enhanced_greeting_1("Mr"))
print(enhanced_greeting_1("Mr")())
print(enhanced_greeting_1("Miss")())


# imperative functions

def my_addition(num1,num2):
    return num1+num2

def my_sub(num1,num2):
    return num1-num2


print(my_addition(1,2))
print(my_sub(1,2))

# lambda functions
add_lambda = lambda num1,num2: num1+num2
print(add_lambda(1,2))

sub_lambda = lambda num1,num2: num1-num2
print(sub_lambda(1,2))

# gen_lambda = lambda num1,num2,op: num1 op num2

# HOF 
def my_operator_definition(op):
    if op == '+':
        return lambda num1,num2: num1+num2
    else:   
        return lambda num1,num2: num1-num2

print(my_operator_definition('+')(1,2))
print(my_operator_definition('-')(1,2))