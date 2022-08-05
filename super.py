class A():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add
 
# Class freelancer inherits EMP
class B(A):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
 
Emp_1 = B(65, "xyz", "India" , "@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)