# global variable
var = 10
m= 10
print("global variable var: ", var)

def return_global_m():
    return m
    

def f():
    # local variable to f() # enclosed variable to f1()
    var1= 100
    m=100
    print("enclosed variable var1: ", var1)
    print("just defined m: ", m)
    
    def f1():
        # local variable to f1()
        var2= 1000
        # nonlocal m # this line tells python that do not create a local variable 
        global m # tells python use global variable
        m=1000
        print("local variable var2: ", var2)
        print("m: ", m)
    f1()    
    print("after calling f1() local m: ", m)
    print("after calling f1() Global m: ",  return_global_m() )
        
f()    