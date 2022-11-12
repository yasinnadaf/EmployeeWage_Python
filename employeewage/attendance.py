import random


class Employee:
    def attendance(self):
        """
        This function will calculate employee attendance.
        :return: None
        """
        is_present = 1
        attendance = random.randint(0, 1)

        if attendance == is_present:
            print('Employee is present')
        else:
            print('Employee is absent')


if __name__ == '__main__':
    emp = Employee()
    emp.attendance()
