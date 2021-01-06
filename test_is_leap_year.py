from is_leap_year import is_leap

def test_is_leap_01():
    total=is_leap(1980)
    assert total == True

def test_is_leap_02():
    total=is_leap(2020)
    assert total == True

def test_is_leap_03():
    total=is_leap(1990)
    assert total == False

def test_is_leap_04():
    total=is_leap(2000)
    assert total == True

def test_is_leap_05():
    total=is_leap(2400)
    assert total == True

def test_is_leap_06():
    total=is_leap(2100)
    assert total == False

def test_is_leap_07():
    total=is_leap(2200)
    assert total == False

def test_is_leap_08():
    total=is_leap(2300)
    assert total == False

def test_is_leap_09():
    total=is_leap(2024)
    assert total == True

def test_is_leap_09():
    total=is_leap(24)
    assert total == True
