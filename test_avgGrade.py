from avgGrade import avgGrade

def test_avgGrade():
    assert avgGrade([51, 57, 53, 95, 60, 87, 90, 62, 87, 95]) == 73.7
    assert avgGrade([62, 98, 58, 56, 66, 58, 81, 98, 55, 59]) == 69.1
    assert avgGrade([90, 60, 95, 58, 66, 66, 66, 51, 84, 74]) == 71.0
    assert avgGrade([53, 77, 70, 89, 98, 95, 90, 60, 54, 98]) == 78.4
    assert avgGrade([64, 77, 65, 91, 66, 74, 61, 62, 58, 90]) == 70.8
