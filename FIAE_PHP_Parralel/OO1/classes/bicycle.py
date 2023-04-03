class Bicycle:
  
  cadence = 0
  speed = 0
  gear = 1
  
  def change_cadence(self, new_value):
    if new_value >= 0:
      self.cadence = new_value
    
  def change_gear(self, new_value):
    if 0 < new_value < 7:
      self.gear = new_value
    
  def speed_up(self, increment):
    self.speed += increment
  
  
  def appl_brakes(self, decrement):
    self.speed -= decrement
   
  def print_state(self):
    print(f"cadence: {self.cadence}\nspeed: {self.speed}\ngear: {self.gear} \n")
    
        
    

