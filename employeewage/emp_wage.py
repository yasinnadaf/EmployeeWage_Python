import csv
import json
import logging
import random

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


class Employee:
    def __init__(self, emp_parameter_dict):
        self.name = emp_parameter_dict.get("employee_name")
        self.wage_per_hr = emp_parameter_dict.get("employee_wage")
        self.total_work_hrs = emp_parameter_dict.get("max_working_hrs")
        self.working_day_per_month = emp_parameter_dict.get("max_working_days")
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

    def get_emp_dict(self):
        """
        Function returns dictionary containing contact attribute values
        :return:
        """
        return {"emp_name": self.name, "working_days": self.working_day_per_month, "total_wage": self.total_wage}

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
        try:
            return self.emp_dict.get(empl_name)
        except Exception as e:
            logging.exception(e)

    def remove_emp(self, empl_name):
        """
        Function deletes existing employee from the employee_dict dictionary
        """
        try:
            if not self.get_emp(empl_name):
                print("Employee not exist")
                return
            self.emp_dict.pop(empl_name)
        except Exception as e:
            logging.exception(e)

    def display_details(self):
        """
        Function to display all employees
        """
        try:
            print("{:<10} {:10} {:10}".format('Employee name', 'Working days', 'Total wage'))
            for name, emp_obj in self.emp_dict.items():
                print(emp_obj.as_string())
        except Exception as e:
            logging.exception(e)

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

    def get_emp_as_dict(self):
        """
        Function get employee details
        :return: details_dict dictionary
        """
        try:
            details_dict = {}
            for key, value in self.emp_dict.items():
                details_dict.update({value.name: value.get_emp_dict()})

            return details_dict
        except Exception as e:
            logging.exception(e)


class MulCompanies:
    def __init__(self):
        self.comp_dic = {}
        self.json_dict = {}

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
        try:
            return self.comp_dic.get(comp_name)
        except Exception as e:
            logging.exception(e)

    def write_to_json_file(self):
        """
        Function to write data to json file

        """
        try:
            for company_name, company_obj in self.comp_dic.items():
                emp_dict = company_obj.get_emp_as_dict()

                self.json_dict.update({company_name: emp_dict})
                json_object = json.dumps(self.json_dict, indent=4)
                with open("emp_wage.json", "w") as write_file:
                    write_file.write(json_object)
        except Exception as e:
            logging.exception(e)

    def write_to_csv_file(self):
        """
        Function to write data to json file

        """
        try:
            with open("emp_wage.csv", "w", newline='') as write_file:
                fieldnames = ['emp_name', 'working_days', 'total_wage']

                csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                for company_name, company_object in self.comp_dic.items():
                    emp_dictionary = company_object.get_emp_as_dict()
                    for key, value in emp_dictionary.items():
                        csv_writer.writerow(value)
        except Exception as e:
            logging.exception(e)


def read_from_json():
    """
    Function to read json file

    """
    with open("emp_wage.json", "r") as read_file:
        json_object = json.load(read_file)
        print(json_object)


def read_from_csv():
    """
    Function for reading csv file
    """
    try:
        with open("emp_wage.csv", "r") as read_csv:
            csv_obj = csv.DictReader(read_csv)
            for rows in csv_obj:
                print(rows)
    except Exception as e:
        logging.exception(e)


def add_employees():
    try:
        company_name = input("Enter company name: ")
        company_obj = multi_comp.comp_dic.get(company_name)
        if not company_obj:
            company_obj = Company(company_name)
            multi_comp.add_company(company_obj)
        emp_name = input("Employee name: ")
        wage_per_hr = int(input("Enter wage per hours: "))
        max_hrs = int(input("Enter maximum working hour: "))
        max_days = int(input("Enter maximum working days: "))
        data_dict = {"employee_name": emp_name, "employee_wage": wage_per_hr, "max_working_days": max_days,
                     "max_working_hrs": max_hrs}
        employee = Employee(data_dict)
        employee.wage_monthly()
        company_obj.add_emp(employee)
        multi_comp.write_to_json_file()
        multi_comp.write_to_csv_file()
    except Exception as e:
        print(e)


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

        multi_comp.write_to_json_file()
        multi_comp.write_to_csv_file()
    except Exception as e:
        print(e)


def display_company():
    """
    function to display company
    """
    try:
        multi_comp.display_comp()
    except Exception as e:
        logging.exception(e)


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

        multi_comp.write_to_json_file()
        multi_comp.write_to_csv_file()
    except Exception as e:
        print(e)


def remove_company():
    """
    Function to remove company
    """
    company_name = input("Enter company name to remove")
    multi_comp.remove_comp(company_name)
    multi_comp.write_to_json_file()
    multi_comp.write_to_csv_file()


if __name__ == '__main__':
    multi_comp = MulCompanies()
    while True:
        choice = int(input("Enter your choice: \n1)add employee  \n2)remove employee \n3)display "
                           "employee\n4)update data  \n5)remove company "
                           "\n6)display company \n7) Read json file\n8) Read csv file\n9)Enter 0 to exit\n"))

        choice_dict = {1: add_employees, 2: delete_employee, 3: disp_employee,
                       4: update_employee, 5: remove_company, 6: display_company, 7: read_from_json, 8: read_from_csv}

        if choice == 0:
            break
        else:
            choice_dict.get(choice)()
