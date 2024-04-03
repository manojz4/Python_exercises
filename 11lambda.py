# # print(create_sandwich(10,1,100))

# def create_sandwich(bread_count,vegetables_kgs,chutney_ml):
#         return f"Sandwich created with bread: {bread_count},vegetables in kgs: {vegetables_kgs},chutney in litres:{chutney_ml} " 
    
# def create_sandwich_without_bread(bread_count):

#     def create_sandwich(vegetables_kgs,chutney_ml):
#         return f"Sandwich created with bread: {bread_count},vegetables in kgs: {vegetables_kgs},chutney in litres:{chutney_ml} " 
    
#     return create_sandwich

# create_sandwich_with_10_bread = create_sandwich_without_bread(10)
# # print(create_sandwich_with_10_bread(1,100))


# create_sandwich_with_20_bread = create_sandwich_without_bread(20)
# # print(create_sandwich_with_20_bread(1,100))

# def create_mayonese_sandwich(older_sandwich_function,input_param1,input_parm2,mayonese_ml):
#     return_val = older_sandwich_function(input_param1,input_parm2)
#     return return_val + "with added mayonese in ml:" + str(mayonese_ml)


# print(create_mayonese_sandwich(create_sandwich_with_10_bread,1,100,89))

####################################################################################

def greeting ():
    return "hello"
    
# print( id(greeting()  )  )
# print(greeting)

# var = greeting
# print(var)


def greeting ():
    return "hello"
    
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


# imperative style        
def my_addition_args(*args):
    sum = 0 
    for val in args:
        sum +=val
    return sum
    
print(my_addition_args(1,2,3)    )
# print(my_addition_args(num1=1,num2=2,num3=3)    )

def my_addition_kwargs(**args):
    sum = 0 
    for val in args.values():
        sum +=val
    return sum

print(my_addition_kwargs(num1=1,num2=2,num3=3)    )
# print(my_addition_kwargs(1,2,3)    )


# HOF with multiple args

def my_operator_definition(op):
    if op == '+':
        def my_addition_args(*args):
            sum = 0 
            for val in args:
                sum +=val
            return sum
        return my_addition_args
    else:   
        def my_sub_args(*args):
            sum = 0 
            for val in args:
                sum -=val
            return sum
        return my_sub_args


print(my_operator_definition('+')(1,2,3))
print(my_operator_definition('-')(1,2,3))


