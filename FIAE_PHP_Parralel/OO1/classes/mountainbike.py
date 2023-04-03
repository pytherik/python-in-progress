from .bicycle import Bicycle

class Mountainbike(Bicycle):
  
  suspension = False
  
  def set_suspension(self, has_suspension):
    self.suspension = has_suspension
    
  def print_state(self):
    if self.suspension:
      print(f"Federung vorhanden.")
    else:
      print("Federung fehlt.")
    return super().print_state()