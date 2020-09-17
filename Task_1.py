from sys import argv

script_name, output, salary, bonus = argv


def payroll():
    res = int(output) * int(salary) + int(bonus)
    print(f'заработная плата сотрудника  {res}')


payroll()
