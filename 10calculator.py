#from function_definitions import *
my_addition = lambda first_number,second_number : first_number+second_number
my_square = lambda first_number, second_number = None : first_number**2
my_exponenation = lambda first_number,second_number : first_number**second_number

def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_addition(first_num,second_num)
        returned_value = hof(my_addition,first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        #returned_value = my_square(first_num)
        returned_value = hof(my_square,first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_exponenation(first_num,second_num)
        returned_value = hof(my_exponenation,first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)


my_calculator()