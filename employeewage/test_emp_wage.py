import pytest

from .emp_wage import Employee, Company, MulCompanies


@pytest.fixture
def employee_obj():
    return Employee({"emp_name": "Raj", "wage_per_hr": 20, "total_work_hrs": 100, "working_day_pm": 20})


@pytest.fixture
def company_obj():
    return Company("Dmart")


@pytest.fixture
def mul_comp_obj():
    return MulCompanies()


def test_add_emp(employee_obj, company_obj):
    assert len(company_obj.emp_dict) == 0
    company_obj.add_emp(employee_obj)
    assert len(company_obj.emp_dict) == 1


def test_delete_emp(employee_obj, company_obj):
    company_obj.add_emp(employee_obj)
    assert employee_obj != company_obj.remove_emp("Raj")


def test_get_employee_method(employee_obj, company_obj):
    company_obj.add_emp(employee_obj)
    company_obj.remove_emp('Raj')
    assert not company_obj.get_emp('Raj')


def test_length_of_company_dictionary(company_obj, mul_comp_obj):
    assert len(mul_comp_obj.comp_dic) == 0
    mul_comp_obj.add_company(company_obj)
    assert len(mul_comp_obj.comp_dic) == 1


def test_get_comp_method(company_obj, mul_comp_obj):
    mul_comp_obj.add_company(company_obj)
    assert company_obj == mul_comp_obj.get_comp('Dmart')


def test_remove_company_method(company_obj, mul_comp_obj):
    mul_comp_obj.add_company(company_obj)
    mul_comp_obj.remove_comp('Dmart')
    assert not mul_comp_obj.get_comp('Dmart')