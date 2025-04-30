# coding:utf-8
# @Time    : 2024/12/19 13:21
# @Author  : Ryan
# @FileName: 员工管理系统.py

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}  # 使用字典来存储员工信息，键为员工ID，值为员工的其他信息

    def add_employee(self, emp_id, name, department):
        if emp_id in self.employees:
            print("Employee already exists.")
        else:
            self.employees[emp_id] = {"Name": name, "Department": department}
            print("Employee added successfully.")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

    def find_employee(self, emp_id):
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print(f"Employee ID: {emp_id}")
            print(f"Name: {emp['Name']}")
            print(f"Department: {emp['Department']}")
        else:
            print("Employee not found.")

    def display_employees(self):
        if self.employees:
            for emp_id, details in self.employees.items():
                print(f"Employee ID: {emp_id}")
                print(f"Name: {details['Name']}")
                print(f"Department: {details['Department']}\n")
        else:
            print("No employees in the system.")

# 创建员工管理系统实例
ems = EmployeeManagementSystem()

# 添加员工
ems.add_employee("001", "Alice", "HR")
ems.add_employee("002", "Bob", "IT")
ems.add_employee("003", "Charlie", "Finance")

# 显示所有员工
ems.display_employees()

# 查找特定员工
ems.find_employee("002")

# 删除员工
ems.remove_employee("001")

# 再次显示所有员工
ems.display_employees()