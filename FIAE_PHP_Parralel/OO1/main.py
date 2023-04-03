from classes.bicycle import Bicycle
from classes.mountainbike import Mountainbike

bike1 = Bicycle()
bike2 = Bicycle()

bike1.change_cadence(10)
bike1.speed_up(15)
bike1.change_gear(3)
bike1.print_state()

bike2.change_cadence(10)
bike2.speed_up(25)
bike2.change_gear(4)
bike2.print_state()

mb1 = Mountainbike()

mb1.set_suspension(True)
mb1.change_cadence(15)
mb1.speed_up(25)
mb1.change_gear(8)
mb1.print_state()