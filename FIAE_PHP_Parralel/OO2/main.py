import os
from pathlib import Path
from classes.employees import Employees


if Path('employees_data.csv').is_file():
    os.remove('employees_data.csv')

persons = [['Hansi', 'Pampel', 1],
           ['Jutta', 'Janüsch', 2],
           ['Bilbo', 'Beutel', 3]]

employees = []
for person in persons:
    employees.append(Employees(person[0], person[1], person[2]))
    employees[-1].store()


def output(new_emps):
    for emp in new_emps:
        print(f"Vorname: {emp.firstname}\nNachname: {emp.lastname}\nId: {emp.department_id}")


emp1 = Employees()
emps = emp1.read()
output(emps)

print(emps[0].firstname)
emps[0].update('firstname', 'Hans-Dietrich')
emps[2].update('lastname', 'Fragnich')
emps[1].update('id', 90210)

emps = emp1.read()

output(emps)
# emps = emps[1].delete()
#
# for emp in emps:
#     print(f"Vorname: {emp.firstname}\nNachname: {emp.lastname}\nId: {emp.department_id}")
