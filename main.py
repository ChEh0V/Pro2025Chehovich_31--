from dataclasses import dataclass
from typing import List, Any, Callable

@dataclass
class Employee:
    id: int
    name: str
    salary: int
    dep_id: int

@dataclass
class Department:
    id: int
    name: str

@dataclass
class EmployeeDepartment:
    dep_id: int
    employee_id: int

def generate_departments() -> List[Department]:
    return [
        Department(1, "Производственный отдел"),
        Department(2, "Отдел кадров"),
        Department(3, "Финансовый отдел"),
        Department(4, "IT отдел"),
        Department(5, "Логистика"),
        Department(6, "Отдел маркетинга"),
    ]

def generate_employees() -> List[Employee]:
    return [
        Employee(1, "Иванов", 50000, 1),
        Employee(2, "Петров", 45000, 1),
        Employee(3, "Сидоров", 60000, 2),
        Employee(4, "Козлов", 55000, 3),
        Employee(5, "Смирнов", 70000, 4),
        Employee(6, "Васильев", 48000, 4),
    ]

def generate_employee_departments() -> List[EmployeeDepartment]:
    return [
        EmployeeDepartment(1, 1),
        EmployeeDepartment(1, 2),
        EmployeeDepartment(2, 3),
        EmployeeDepartment(3, 4),
        EmployeeDepartment(4, 5),
        EmployeeDepartment(4, 6),
        EmployeeDepartment(6, 1),
        EmployeeDepartment(6, 3),
    ]

def print_data(data: List[Any], headers: List[str], title: str, column_width: int = 20) -> None:
    total_length = len(headers) * column_width

    print(f"{title:=^{total_length}}")
    print("".join(f"{header:<{column_width}}" for header in headers))
    print("-" * total_length)

    for row in data:
        if isinstance(row, tuple):
            print("".join(f"{str(item):<{column_width}}" for item in row))
        else:
            print(f"{str(row):<{total_length}}")
    print()

def first_query(departments: List[Department], employees: List[Employee]) -> List[Any]:
    result = []
    for emp in employees:
        for dep in departments:
            if emp.dep_id == dep.id:
                result.append((emp.name, emp.salary, dep.name))
    result.sort(key=lambda x: x[2])
    return result

def second_query(departments: List[Department], employees: List[Employee]) -> List[Any]:
    dep_salaries = {}
    for dep in departments:
        dep_salaries[dep.id] = 0
    for emp in employees:
        if emp.dep_id in dep_salaries:
            dep_salaries[emp.dep_id] += emp.salary
    result = []
    for dep in departments:
        result.append((dep.name, dep_salaries.get(dep.id, 0)))
    result.sort(key=lambda x: x[1])
    return result

def third_query(departments: List[Department], employees: List[Employee],
                relations: List[EmployeeDepartment], condition: Callable) -> List[Any]:
    dep_employees = {}
    for dep in departments:
        if condition(dep.name):
            dep_employees[dep.id] = []
    for rel in relations:
        if rel.dep_id in dep_employees:
            dep_employees[rel.dep_id].append(rel.employee_id)
    result = []
    for dep in departments:
        if dep.id in dep_employees:
            for emp_id in dep_employees[dep.id]:
                for emp in employees:
                    if emp.id == emp_id:
                        result.append((dep.name, emp.name, emp.salary))
    return result

def main() -> None:
    departments = generate_departments()
    employees = generate_employees()
    relations = generate_employee_departments()

    print("="*60)
    print("Отрефакторенная программа РК №1")
    print("="*60)

    print_data(
        first_query(departments, employees),
        ["Сотрудник", "Зарплата", "Отдел"],
        "Запрос 1: Сотрудники по отделам"
    )

    print_data(
        second_query(departments, employees),
        ["Отдел", "Суммарная зарплата"],
        "Запрос 2: Суммарная зарплата по отделам"
    )

    print_data(
        third_query(departments, employees, relations,
                   lambda name: "отдел" in name.lower()),
        ["Отдел", "Сотрудник", "Зарплата"],
        "Запрос 3: Сотрудники в отделах, содержащих 'отдел'"
    )

if __name__ == "__main__":
    main()
