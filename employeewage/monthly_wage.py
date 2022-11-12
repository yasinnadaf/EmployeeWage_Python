import random


class Employee:

    def wage_monthly(self):
        """
        This function will calculate employee wage.
        :return: Employee attendance.
        """
        is_present = 1
        is_part_time = 2
        wage_per_hr = 20
        full_day_hr = 8
        part_time_hr = 4
        working_day_per_month = 20
        is_absent = 0
        emp_absent = 0

        monthly_wage = 0

        for day in range(1, working_day_per_month+1):
            attendance = random.randint(0, 2)
            if attendance == is_present:
                print('day:', day)
                # print('Employee is present')
                daily_wage = full_day_hr * wage_per_hr
                print(f'Employee is present and its wage is:{daily_wage}')

            elif attendance == is_part_time:
                print('day:', day)
                # print('Employee is working part-time')
                daily_wage = wage_per_hr * part_time_hr
                print(f'Employee is working part-time and its wage is:{daily_wage}')

            else :
                attendance == is_absent
                daily_wage = emp_absent * wage_per_hr
                print('day:', day)
                print(f'Employee is absent and its wage is:{daily_wage}')
            monthly_wage += daily_wage

        print('\n------> Monthly Wage <-------')
        print (f'{monthly_wage:14}')


if __name__ == '__main__':
    emp = Employee()
    emp.wage_monthly()
