from employee import get_employee_info

def test_get_employee_info():
    result = get_employee_info("Alice", "E101", "IT", 55000)

    expected = (
        "Employee Name: Alice\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )

    assert result == expected