import employee_info
import pytest

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result==pytest.approx(60166.67)

def test_get_employees_by_age_range():
    result =employee_info.get_employees_by_age_range(25,35)
    assert len(result)== 2
    assert [i["name"] for i in result] ==["John", "Mike"]

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Marketing")
    assert len(result) ==2
    assert [i["name"] for i in result] ==["Jane", "Mary"]