# #creating a dictionary 
# d = {'name': 'Gaurav' , 'rollno' : 1 ,'rollno' : 2}
# print(d)

# d= dict(name = 'Sagar' , rollno = 2 )
# print(d)

# d= dict([('name','Deepak') ,( 'rollno' , 3 ),('admission year', 2017)])
# print(d)

# #d= {}
# #no_of_items = int(input("How many items you want to add"))
# #for i in range(0,no_of_items,1):
# #    key = input('Please enter the key ')    
# #    value = input('Please enter the value ')    
# #    d[key] = value # d.update({key:value})

# #print(d)

# #adding to a blank dictionary 
# d= {}
# keys = input("Please enter keys comma separated :").split(",")
# values= input("Please enter values comma separated :").split(",")

# for i in range(0,len(keys)) :
#     d[keys[i]] = values[i]

# print(d)

# #SELECT
# d={'employee_id' : 100, 'address': ['pune', 'maharashtra']}

# print("Employee id is :", d['employee_id'])
# print("Employee id1 is :", d['employee_id1'])

# print("The employee id is", d.get('employee_id'))
# print("The employee id1 is " , d.get('employee_id1'))
# print("The employee id1 is " ,d.get("employee_id1","Default_value"))



#######################################################################

d={'name':'manoj','id': '1'}
d.update({"city":'pune',"state":'maharashtra'})
print(d)


#remove
del d["city"]
print(d)

d.popitem()
print(d)
d.pop('name')  
print(d)


#update
d|= {"id":505067} 
print(d)
     
d.update( {"id":47}  )
print(d)

# utility

print('no_of_keys', len(d))
new_copy = d.copy()
print('d address:',id(d), 'new_copy address:',id(new_copy))

new_copy.update({'doctor_name': 'god'})
print('reversed dictionary :  ', list(reversed(new_copy.items())))

print("current_val:", new_copy.setdefault('doctor_name',"krishna pawara"))
print("current_val:", new_copy.setdefault('nurse_name',"krishna pawara"))
print(new_copy)

print(dict.fromkeys(['name',"address"],"blank"))     






