import random


class Employee:
    def __init__(self, name, wage_per_hr=20, total_work_hrs=100, working_day_pm=20):
        self.wage_per_hr = wage_per_hr
        self.total_work_hrs = total_work_hrs
        self.working_day_per_month = working_day_pm
        self.name = name

    def get_daily_wage(self, attendance):
        if attendance == 1:
            hr = 8
        elif attendance == 2:
            hr = 4
        else:
            hr = 0
        daily_wage = hr * self.wage_per_hr
        return daily_wage, hr

    def wage_monthly(self):
        """
        This function will calculate employee wage.
        :return: Employee attendance.
        """
        total_hrs = 0
        day = 0
        total_wage = 0

        while total_hrs<self.total_work_hrs and day<self.working_day_per_month:
            attendance = random.randint(0, 2)
            daily_wage, hr = self.get_daily_wage(attendance)

            total_wage += daily_wage
            total_hrs += hr
            day += 1

        print('total work hour is: ', total_hrs)
        print('total work day are: ', day)
        print('total wage is: ', total_wage)


if __name__ == '__main__':
    emp = Employee('sujit')
    emp.wage_monthly()
