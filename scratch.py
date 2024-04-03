# def f1():
#     print(1+"hello")
    
# def f ():
#     try:
#         f1()
#     except Exception:
#         print("I am inside exception block") 
# f() 

###############################################


try:
    input_var = int(input("Please enter a number "))
except Exception:
    try:
        input_var = int(input("You entered an incorrect number , Please try again ! "))
    except :
        input_var = int(input("You stupid please enter a number"))    
print("Adding 10 to your value entered is " , input_var+ 10)

#################################################



