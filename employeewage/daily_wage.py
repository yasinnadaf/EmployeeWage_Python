import random


class Employee:
    def wage_daily(self):
        """
        This function will calculate employee daily wage.
        :return: Employee attendance
        """
        is_present = 1
        wage_per_hr = 20
        full_day_hr = 8

        attendance = random.randint(0, 1)
        if attendance == is_present:
            print('Employee is present')
            daily_wage = full_day_hr * wage_per_hr
            print('daily wage is: ', daily_wage)
        else:
            print('Employee is absent')


if __name__ == '__main__':
    emp = Employee()
    emp.wage_daily()
