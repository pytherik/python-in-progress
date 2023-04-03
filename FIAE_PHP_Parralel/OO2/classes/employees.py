class Employees:
  
  def __init__(self, firstname, lastname, department_id):
    self.firstname = firstname
    self.lastname = lastname
    self.department_id = department_id
    
  def set_firstname(self, firstname):
    self.firstname = firstname
    
  def get_firstname(self):
    print(self.firstname)
    
  def set_lastname(self, lastname):
    self.lastname = lastname
    
  def get_lastname(self):
    print(self.lastname)
    
  def set_department_id(self, department_id):
    self.department_id = department_id
    
  def get_department_id(self):
    print(self.department_id)
    
  def store(self):
    with open("employees_data.csv", "a") as f:
      f.write(f"{self.firstname},{self.lastname},{self.department_id}\n")
    print(f"Employee {self.department_id} stored")
    