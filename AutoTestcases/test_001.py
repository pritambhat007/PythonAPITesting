import pytest
import tesults


compare_test = "Test"
@pytest.fixture()
def fixture_code():
    print("This is start of test cases")
    print("----------------------------")
    yield
    print("This is end of test cases")
    print("---------------------------")


def test_case_1(fixture_code):
    print("This is first test case")
    assert compare_test == "fail" , "These 2 values must be same"

def test_case_2(fixture_code):
    print("This is second test case")
