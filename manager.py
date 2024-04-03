from employee import Employee

class Manager(Employee):
    
    # instances veriables
    def __init__(self, id, name, blocation, dlocation, post,sal ,employees):
        super().__init__(id, name, blocation, dlocation, post , sal)
        
        self.managed_employees = employees
    
    
    # instances methods
    def perform_appraisal_for_an_employee(emp_reference,percent_raise):
        emp_reference.salary = (emp_reference.salary / percent_raise ) + emp_reference.salary
        return emp_reference.salary
    
    # instances methods
    def get_manager_details(self):
        return self.emp_id, self.emp_name, self.base_location, self.dployed_location, self.designation, self.salary , self.managed_employees


def main():
    employees = []

    
    print(" Employee Details ")

    for i in range (0,2):
        
        id = int(input("enter the id : "))
        name = input("enter the name : ")
        blocation = input("enter the blocation : ")
        dlocation = input("enter the dlocation : ")
        post = input("enter the post : ")
        sal = int(input("enter the salary : " ))
        
        employee = Employee(id,name,blocation,dlocation,post,sal)
        print(employee.emp_id , employee.emp_name)
        employees.append(employee)
        print("employee added successfully ........")
        
    # print(employees[0].emp_id)


    # manger details 
    print(" Manager Details ")
    id = int(input("enter the id : "))
    name =  input("enter the name : ")
    blocation = input("enter the blocation : ")
    dlocation = input("enter the dlocation : ")
    post = input("enter the post : ")
    sal = int(input("enter the salary : " ))

    manager = Manager(id ,name ,blocation ,dlocation ,post ,sal , employees)
    print("Manager created successfully ........")

    setSalary = Manager.perform_appraisal_for_an_employee(manager.managed_employees[0] , 10 )
    print( "Incremented  Salary of employee"  ,setSalary)

    # print(manager.managed_employees[0].)
    managerdetails =  manager.get_manager_details()
    print( "Manager details " , managerdetails)
    


if __name__ == "__main__":
    main()