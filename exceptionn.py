# hard_code= {
#      1: "red" , 2: "Blue" , 3: "Orange"
#  }

# try:
#      print(hard_code[int(input("key:"))])
# except KeyError:
#      print("Key not found")    

# hard_code = [1,2,3,4,5]
# try:
#       print(hard_code[int(input("Index:"))])
# except:
#             print("Index does not exists")    

# class new_exception(Exception):
#      pass

# if int(input("age"))*365 > 100001 :
#      raise new_exception
# else:
#     print("value is less than 100001")
    
    ########################################################
    
  # my custom exception created 
class negative_number_error(Exception):
    pass

def create_positive_numbered_list(my_list):
    """
    1) Create a postive numbered list 
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    """
    for cntr in range(0,int(input("Please enter number of elements to the positive numbered list"))):
        num = int(input("Please enter a number to be added ")) 
        if (num ) <0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# my custom exception created 
class positive_number_error(Exception):
    pass

def create_negative_numbered_list(my_list):
    """
    2) Create a negative  numbered list 
    Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
    """
    for cntr in range(0,int(input("Please enter number of elements to the negative numbered list"))):
        num = int(input("Please enter a number to be added "))
        if num >0:
            raise  positive_number_error
        else:
            my_list.append(num)
    print(my_list)   

# my custom exception created 
class homogenous_list_error(Exception):
    pass



def value_provider(element):
    datatype_choice = int(input(f"Please choose a datatype of the {element} to be added \
        \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

    if datatype_choice == 1:
        ret_val = int(input("Please enter an integer to be added "))
    if datatype_choice == 2:
        ret_val = float(input("Please enter a float to be added "))
    if datatype_choice == 3:
        ret_val = input("Please enter a string to be added ")
    if datatype_choice == 4:
        ret_val = tuple(input("Please enter a tuple to be added like 1,2 ").split(","))
    if datatype_choice == 5:
        ret_val = input("Please enter a list to be added like 1,2,3,4 ").split(",")
    if datatype_choice == 6:
        ret_val = set(input("Please enter a set to be added like 1,2 ").split(","))
    if datatype_choice == 7:
        my_temp_dict = {}
        keys = input("Please enter the keys of the dictionary to be added like key1,key2 ").split(",")
        for key in keys : 
            my_temp_dict[key] = value_provider('key'+key)
        ret_val = my_temp_dict
    return ret_val

def create_heterogenous_list(my_list):
    """    3) Create a heterogenous list 
    Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
    """
    for cntr in range(0,int(input("Please enter number of elements to the heterogenous list"))):
        my_list.append(value_provider('Index'+str(cntr)))
    print(my_list)   
    
    # check if we are have a homogenous list  
    is_homogenous = True
    for subscript in range(1,len(my_list)):
        if  type(my_list[0]) != type(my_list[subscript]):
            is_homogenous = False
            break
        
    if is_homogenous:
        raise homogenous_list_error
    else:
        print("We received a Heterogenous list ")       

def find_an_element(my_list):
    
    datatype_choice = int(input("""Please choose a datatype of the element to be searched \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n """))

    print(datatype_choice)
    if datatype_choice == 1:
        input_val = int(input("Please enter an integer  "))
    if datatype_choice == 2:
        input_val = float(input("Please enter a float "))
    if datatype_choice == 3:
        input_val = input("Please enter a string ")
    if datatype_choice == 4:
        input_val = tuple(input("Please enter a tuple like 1,2 ").split(","))
    if datatype_choice == 5:
        input_val = input("Please enter a list like 1,2,3,4 ").split(",")
    if datatype_choice == 6:
        input_val = set(input("Please enter a set like 1,2 ").split(","))
    if datatype_choice == 7:
        my_temp_tuple_list = []
        for str_elem in input("Please enter a dictionary like key1:value1,key2:value2 ").split(","):
            my_temp_tuple_list.append(tuple(str_elem.split(":")))
            input_val = dict(my_temp_tuple_list)
    
    print(f"{input_val} found in provided list {my_list} : {input_val in my_list}")
    
# invocation 

def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Refresh the program to start with blank lists")
            print("5) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            elif choice ==4:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==5:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()      