#When two or more methods in the same class have the same name but different parameters, it’s called Overloading.
#Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. 
#Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.

#Example
# Function to take multiple arguments  
def add(datatype, *args):  
    
    # if datatype is int  
    # initialize answer as 0  
    if datatype =='int':  
        answer = 0
            
    # if datatype is str  
    # initialize answer as ''  
    if datatype =='str':  
        answer =''  
    
    # Traverse through the arguments  
    for x in args:  
    
        # This will do addition if the   
        # arguments are int. Or concatenation   
        # if the arguments are str  
        answer = answer + x  
    
    print(answer)  
    
# Integer  
add('int', 5, 6)  
    
# String  
add('str', 'Hi ', 'Geeks') 


#When the method signature (name and parameters) are the same in the superclass and the child class, it’s called Overriding
#Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. 
#It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. 
#In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.

#Example
class A: 
  
    def fun1(self): 
        print('feature_1 of class A') 
          
    def fun2(self): 
        print('feature_2 of class A') 
      
  
class B(A): 
      
    # Modified function that is  
    # already exist in class A 
    def fun1(self): 
        print('Modified feature_1 of class A by class B')     
          
    def fun3(self): 
        print('feature_3 of class B') 
          
  
# Create instance 
obj = B() 
      
# Call the override function 
obj.fun1() 
