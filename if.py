a = int(input("a : "))
g = input("m/f : ")
if((a ==1 or a ==2) and g == "m"):
    print("fee is 100")
elif (a == 3 or a ==4 or g =="f" ):
    print("fee is 200")
elif (a == 5 or g =="m" ):
    print("fee is 300")  
else:
    print("no fee")  
