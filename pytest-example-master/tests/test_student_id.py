from myapp.mymodule.funcs import multiply

def test_student_id_last_two_digits():
    expected = 37 
    a, b = expected, 1
    assert multiply(a, b) == expected
