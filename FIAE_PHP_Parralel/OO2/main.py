from classes.employees import Employees

persons = [['Hansi', 'Pampel', 1],
           ['Jutta', 'Janüsch', 2],
           ['Bilbo', 'Beutel', 3]]

employees = []
for person in persons:
    employees.append(Employees(person[0], person[1], person[2]))
    employees[-1].store()

emp1 = Employees()
emps = emp1.read()


for emp in emps:
    print(f"Vorname: {emp.firstname}\nNachname: {emp.lastname}\nId: {emp.department_id}")

# emps = emps[1].delete()
#
# for emp in emps:
#     print(f"Vorname: {emp.firstname}\nNachname: {emp.lastname}\nId: {emp.department_id}")
