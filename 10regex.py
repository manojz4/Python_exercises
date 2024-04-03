import re

"""
[] . ^ $ * + ? {}
() \ |

#\w - Matches any alphanumeric character (digits and alphabets and underscore). 
    #\d - Matches any decimal digit. Equivalent to [0-9]
    #\s - Matches where a string contains any whitespace character.
    # Equivalent to [ \t\n\r\f\v].

"""
#------------------------------------
# DEMO 
#------------------------------------
import re
string0 = "abcdefghijklmnopqrstuvwxyz"
string1 = "abcdefghijklmnopqrstuvwxyz1234567890"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string3 = "0123456789"
string4 = "HELLO HEL "
string5 = "hello hel"
string6 = "hello123"
string14 = "hello123h"
string7 = "123hello"
string8 = "__"
string9 = "......"
string10 = "**************"
string11 = "```````````````"
string12 = "!!!!!!!!!!!"
string13 = ""
string15 = "abcdef highkl"
string16 = "a430928409238409234"
string17 = "a4"

my_list = [string0,string1,string2,string3,string4,string5,string6,string14,string7,string8,string9,string10,string11,string12,string13,string15,string16,string17]
   
for test_string in my_list:
    result = re.findall(r"[a-z]+?$", test_string, re.IGNORECASE)  
    search_obj = re.search(r"[arn]", test_string)  
    if search_obj is not None :
        print(f"{test_string} resulted into {result}")  
        print(f"{test_string} resulted into {search_obj}")  
   