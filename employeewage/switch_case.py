import random


class Employee:
    def __init__(self, wage_per_hr):
        self.wage_per_hr = wage_per_hr

    def wage_calculate(self):
        """
        This function will calculate employee wage.
        :return: Employee attendance.
        """
        rand = random.randint(0, 2)
        emp_hrs = self.emp_hrs(rand)
        emp_wage = emp_hrs * self.wage_per_hr
        print(f'Employee wage is {emp_wage}')

    def emp_hrs(self, hr):
        switcher = {
            0: 0,
            1: 8,
            2: 4
        }
        return switcher.get(hr)


if __name__ == '__main__':
    emp = Employee(20)
    emp.wage_calculate()
