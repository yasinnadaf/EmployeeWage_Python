import random


class Employee:
    def daily_wage(self):
        """
        This function will calculate employee part-time wage.
        :return: Employee attendance.
        """
        is_present = 1
        is_part_time = 2
        wage_per_hr = 20
        full_day_hr = 8
        part_time_hr = 4

        attendance = random.randint(0, 2)
        if attendance == is_present:
            print('Employee is present')
            daily_wage = full_day_hr * wage_per_hr
            print('daily wage is: ', daily_wage)

        elif attendance == is_part_time:
            print('Employee is working part time')
            daily_wage = wage_per_hr * part_time_hr
            print('part time wage is: ', daily_wage)
        else:
            print('Employee is absent')


if __name__ == '__main__':
    emp = Employee()
    emp.daily_wage()
