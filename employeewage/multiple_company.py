import logging
import random

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


class Employee:
    def __init__(self, employee_name, wage_per_hr=20, total_work_hrs=100, working_day_pm=20):
        self.wage_per_hr = wage_per_hr
        self.total_work_hrs = total_work_hrs
        self.working_day_per_month = working_day_pm
        self.name = employee_name
        self.total_wage = 0

    def get_daily_wage(self, attendance):
        """
        Function to check employee working hours

        """
        try:
            if attendance == 1:
                hr = 8
            elif attendance == 2:
                hr = 4
            else:
                hr = 0
            return hr
        except Exception as e:
            logging.exception(e)

    def as_string(self):
        return "{:^14} {:^10} {:^14}".format(self.name, self.working_day_per_month, self.total_wage)

    def wage_monthly(self):
        """
        This function will calculate employee wage.
        :return: Employee attendance.
        """
        total_hrs = 0
        day = 0

        try:
            while total_hrs < self.total_work_hrs and day < self.working_day_per_month:
                attendance = random.randint(0, 2)
                hr = self.get_daily_wage(attendance)
                self.total_wage += self.wage_per_hr * hr
                total_hrs += hr
                day += 1
        except Exception as e:
            logging.exception(e)


class Company:
    def __init__(self, comp_name):
        self.name = comp_name
        self.emp_dict = {}

    def add_emp(self, emp_obj):
        """
        This function add employee data to the company
        :return:none
        """
        try:
            self.emp_dict.update({emp_obj.name: emp_obj})
        except Exception as e:
            logging.exception(e)

    def get_emp(self, empl_name):
        """
        Function to get employee object
        :param empl_name: string
        :return: Employee object
        """

        return self.emp_dict.get(empl_name)

    def remove_emp(self, empl_name):
        """
        Function deletes existing employee from the employee_dict dictionary
        :return:
        """
        if not self.get_emp(empl_name):
            print("Employee not exist")
            return
        self.emp_dict.pop(empl_name)

    def display_details(self):
        """
        Function to display all employees
        """
        print("{:<10} {:10} {:10}".format('Employee name', 'Working days', 'Total wage'))
        for name, emp_obj in self.emp_dict.items():
            print(emp_obj.as_string())

    def update(self, employee_obj, data_dict):
        """
        Function to update employee information in employee_dict dictionary

        """
        try:
            employee_obj.emp_name = data_dict.get("update_name")
            employee_obj.wage = data_dict.get("update_wage")
            employee_obj.maxi_days = data_dict.get("update_days ")
            employee_obj.max_hours = data_dict.get("updated_hours")

        except Exception as e:
            logging.exception(e)


class MulCompanies:
    def __init__(self):
        self.comp_dic = {}

    def add_company(self, obj_of_comp):
        """
        This function add company object to company dictionary

        """
        try:
            self.comp_dic.update({obj_of_comp.name: obj_of_comp})
        except Exception as e:
            logging.exception(e)

    def display_comp(self):
        """
        This function display the employee data of a company

        """
        try:
            for name, obj_of_comp in self.comp_dic.items():
                print('company name: ', name)
        except Exception as e:
            logging.exception(e)

    def remove_comp(self, comp_name):
        """
        This function deletes the company from the dictionary

        """
        try:
            if comp_name in self.comp_dic:
                self.comp_dic.pop(comp_name)
            else:
                print('company not exist')
        except Exception as e:
            logging.exception(e)

    def get_comp(self, comp_name):
        """
        This function retrieve data of a Company

        """
        return self.comp_dic.get(comp_name)


def add_employees():
    company_name = input("Enter company name: ")
    company_obj = multi_comp.comp_dic.get(company_name)
    if not company_obj:
        company_obj = Company(company_name)
        multi_comp.add_company(company_obj)
    emp_name = input("Employee name: ")
    wage_pr_hr = int(input("Enter wage per hours: "))
    max_hrs = int(input("Enter maximum working hour: "))
    max_days = int(input("Enter maximum working days: "))
    employee = Employee(emp_name, wage_pr_hr, max_hrs, max_days)
    employee.wage_monthly()
    company_obj.add_emp(employee)


def disp_employee():
    """
    Function to display employee names
    """
    try:
        com_name = input("Enter company to view employees : ")
        company_obj = multi_comp.get_comp(com_name)
        if not company_obj:
            print("--> company not found or deleted <--")
            return
        company_obj.display_details()
    except Exception as e:
        print(e)


def delete_employee():
    """
    Function to delete employee
    """
    try:
        compan_name = input("Enter company to delete employees : ")
        company_obj = multi_comp.get_comp(compan_name)
        employee_name = input("Enter employee name : ")
        company_obj.remove_emp(employee_name)
    except Exception as e:
        print(e)


def display_company():
    """
    function to display company
    """
    multi_comp.display_comp()


def update_employee():
    """
    Function to update employee details
    """
    try:
        comp_name_to_update = input("Enter company to update employee information : ")
        company_ob = multi_comp.get_comp(comp_name_to_update)
        if not company_ob:
            print("Company not exist")
            return
        employee_name = input("Enter employee name to update : ")
        emp_object = company_ob.get_emp(employee_name)
        if not emp_object:
            print("Employee not present")
        else:
            update_wage = int(input("Enter wage to update : "))
            update_working_days = int(input("Enter  working days to update : "))
            update_working_hrs = int(input("Enter working hours to update : "))

            company_ob.update(emp_object, {"update_name": employee_name, "update_wage": update_wage,
                                           "update_days": update_working_days, "update_hours": update_working_hrs})
    except Exception as e:
        print(e)


def remove_company():
    """
    Function to remove company
    """
    company_name = input("Enter company name to remove")
    multi_comp.remove_comp(company_name)


if __name__ == '__main__':
    multi_comp = MulCompanies()
    while True:
        choice = int(input("Enter your choice: \n1)add employee  \n2)remove employee \n3)display "
                           "employee\n4)update data  \n5)remove company \n6)display company \n"
                           "7)exit\n"))

        choice_dict = {1: add_employees, 2: delete_employee, 3: disp_employee,
                       4: update_employee, 5: remove_company, 6: display_company}

        if choice == 0:
            break
        elif choice > 8:
            print("Enter correct choice")
        else:
            choice_dict.get(choice)()

