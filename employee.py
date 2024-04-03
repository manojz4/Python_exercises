class Employee:
    
    def get_org_name(self,orgname):
        self.org_name = orgname
        
    def rcv_org_name(self):
        return self.org_name
    
    def __init__(self,id,name,blocation,dlocation,post,sal):
        self.emp_id= id
        self.emp_name= name
        self.base_location= blocation
        self.dployed_location = dlocation
        self.designation = post
        self.salary = sal
        
    def rcv_employee_detail(self):
        return self.emp_id, self.emp_name, self.base_location, self.dployed_location, self.designation, self.salary
    
def main():
    
    # e1=Employee()
    emp = input("Enter id: ")
    name= input("Enter name: ")
    blo = input("Enter base location: ")
    dlo = input("Enter destion location: ")
    pos = input("Enter desgination: ")
    sal = input("Enter sal: ")
    
    e1=Employee(emp,name,blo,dlo,pos,sal)
    
    a,b,c,d,e,f = e1.rcv_employee_detail()
    
    print("Id: ",a)
    print("Name: ",b)
    print("Base location: ",c)
    print("Destion location: ",d)
    print("Desgination: ",e)
    print("Sal: ",f)
    

if __name__ == "__main__":
    main()   