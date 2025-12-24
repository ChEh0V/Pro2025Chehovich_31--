import pytest
from main import Employee, Department, EmployeeDepartment, first_query, second_query, third_query


@pytest.fixture
def test_data():
    departments = [
        Department(1, "Производственный отдел"),
        Department(2, "Отдел кадров"),
        Department(3, "IT отдел"),
        Department(4, "Логистика"),
    ]

    employees = [
        Employee(1, "Иванов", 50000, 1),
        Employee(2, "Петров", 45000, 1),
        Employee(3, "Сидоров", 60000, 2),
        Employee(4, "Козлов", 55000, 3),
        Employee(5, "Смирнов", 70000, 4),
    ]

    relations = [
        EmployeeDepartment(1, 1),
        EmployeeDepartment(1, 2),
        EmployeeDepartment(2, 3),
        EmployeeDepartment(3, 4),
        EmployeeDepartment(4, 5),
        EmployeeDepartment(2, 1),
        EmployeeDepartment(3, 2),
    ]

    return departments, employees, relations


def test_first_query_basic(test_data):
    departments, employees, _ = test_data
    result = first_query(departments, employees[:3])


    assert len(result) == 3
    for item in result:
        assert len(item) == 3
        assert isinstance(item[0], str)
        assert isinstance(item[1], int)
        assert isinstance(item[2], str)


def test_second_query_basic(test_data):
    departments, employees, _ = test_data
    result = second_query(departments, employees)

    assert len(result) == 4  # Для 4 отделов
    for item in result:
        assert len(item) == 2
        assert isinstance(item[0], str)
        assert isinstance(item[1], int)


def test_third_query_basic(test_data):
    departments, employees, relations = test_data
    result = third_query(
        departments,
        employees,
        relations,
        lambda name: "отдел" in name.lower()
    )
    assert len(result) > 0
    for item in result:
        assert len(item) == 3
        assert "отдел" in item[0].lower()


def test_main_program():

    try:
        from main import main
        main()
        assert True
    except Exception as e:
        pytest.fail(f"Программа вызвала исключение: {e}")
