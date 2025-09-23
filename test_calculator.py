import calculator

def test_add():
    assert calculator.add(2,3) == 5
    assert calculator.add(-1,1) == 0

def test_sub():
    assert calculator.sub(5, 2) == 3
    assert calculator.sub(0, 3) == -3

def test_mul():
    assert calculator.mul(3, 4) == 12
    assert calculator.mul(-2, 3) == -6

def test_div():
    assert calculator.div(10, 2) == 5
    try:
        calculator.div(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

# Run tests when executed directly
if __name__ == "__main__":
    test_add()
    test_sub()
    test_mul()
    test_div()
    print("All tests passed ✅")
