import pytest
import employee_info


def test_calculate_average_salary():
    assert employee_info.calculate_average_salary() == pytest.approx(60166.666666666664)


@pytest.mark.parametrize("department, names", [("Sales", ["John", "Peter"]), ("Marketing", ["Jane", "Mary"]), ("Engineering", ["Chloe", "Mike"]), ("Unknown", [])])
def test_get_employees_by_dept(department, names):
    assert [item["name"] for item in employee_info.get_employees_by_dept(department)] == names


@pytest.mark.parametrize("lower, upper, names", [(25, 35, ["John", "Mike"]), (20, 41, ["John", "Jane", "Mary", "Chloe", "Mike", "Peter"]), (30, 30, []), (40, 20, []), ("25", "35", ["John", "Mike"])])
def test_get_employees_by_age_range(lower, upper, names):
    # Preserve the starter function's exclusive lower/upper bounds.
    assert [item["name"] for item in employee_info.get_employees_by_age_range(lower, upper)] == names


def test_empty_employee_data(monkeypatch):
    monkeypatch.setattr(employee_info, "employee_data", [])
    assert employee_info.calculate_average_salary() == 0
    assert employee_info.get_employees_by_dept("Sales") == []
    assert employee_info.get_employees_by_age_range(20, 40) == []
