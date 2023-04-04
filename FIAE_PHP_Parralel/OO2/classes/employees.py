from pathlib import Path
import os


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

        # print(f"Size: {os.stat('employees_data.csv').st_size}")
        if Path('employees_data.csv').is_file() and os.stat('employees_data.csv').st_size > 0:
            separator = "\n"
        else:
            separator = ""
        with open('employees_data.csv', 'a') as f:
            f.write(f"{separator}{self.firstname},{self.lastname},{self.department_id}")
        print(f"Employee {self.department_id} stored")

    @staticmethod
    def read():

        if Path('employees_data.csv').is_file():
            with open('employees_data.csv', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

