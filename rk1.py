from operator import itemgetter

class Employee:
    def __init__(self, id, name, salary, dep_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.dep_id = dep_id

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class EmployeeDepartment:
    def __init__(self, dep_id, employee_id):
        self.dep_id = dep_id
        self.employee_id = employee_id

departments = [
    Department(1, "Производственный отдел"),
    Department(2, "Отдел кадров"),
    Department(3, "Финансовый отдел"),
    Department(4, "IT отдел"),
    Department(5, "Логистика"),
    Department(6, "Отдел маркетинга"),
]

employees = [
    Employee(1, "Иванов", 50000, 1),
    Employee(2, "Петров", 45000, 1),
    Employee(3, "Сидоров", 60000, 2),
    Employee(4, "Козлов", 55000, 3),
    Employee(5, "Смирнов", 70000, 4),
    Employee(6, "Васильев", 48000, 4),
]

employees_departments = [
    EmployeeDepartment(1, 1),
    EmployeeDepartment(1, 2),
    EmployeeDepartment(2, 3),
    EmployeeDepartment(3, 4),
    EmployeeDepartment(4, 5),
    EmployeeDepartment(4, 6),
    EmployeeDepartment(6, 1),
    EmployeeDepartment(6, 3),
]

def main():
    one_to_many = [(e.name, e.salary, d.name)
        for d in departments
        for e in employees
        if e.dep_id == d.id]

    many_to_many_temp = [(d.name, ed.dep_id, ed.employee_id)
        for d in departments
        for ed in employees_departments
        if d.id == ed.dep_id]

    many_to_many = [(e.name, e.salary, dep_name)
        for dep_name, dep_id, employee_id in many_to_many_temp
        for e in employees if e.id == employee_id]

    print("Задание 1")
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(*res_1, sep='\n')

    print("\nЗадание 2")
    res_2_unsorted = []
    for d in departments:
        d_employees = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_employees) > 0:
            d_salaries = [s for _, s, _ in d_employees]
            d_salaries_sum = sum(d_salaries)
            res_2_unsorted.append((d.name, d_salaries_sum))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(*res_2, sep='\n')

    print("\nЗадание 3")
    res_3 = {}
    for d in departments:
        if 'отдел' in d.name.lower():
            d_employees = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_employees_names = [n for n, _, _ in d_employees]
            res_3[d.name] = d_employees_names
    print(res_3)

if __name__ == "__main__":
    main()
