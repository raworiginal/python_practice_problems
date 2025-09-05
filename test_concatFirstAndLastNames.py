
from concatFirstAndLastNames import concatFirstAndLastNames
first_names1 = ["Peter", "Tony", "Steve", "Natasha", "Bruce", "Thor", "Wanda", "Scott", "Stephen"]
last_names1 = ["Parker", "Stark", "Rogers", "Romanoff", "Banner", "Odinson", "Maximoff", "Lang", "Strange"]

first_names2 = ["Bruce", "Clark", "Diana", "Barry", "Hal", "Oliver", "Arthur", "Victor", "Billy", "John"]
last_names2 = ["Wayne", "Kent", "Prince", "Allen", "Jordan", "Queen", "Curry", "Stone", "Batson", "Constantine"]

def test_concatFirstAndLastNames():
    assert concatFirstAndLastNames(first_names1,last_names1) == ['Peter Parker', 'Tony Stark', 'Steve Rogers', 'Natasha Romanoff', 'Bruce Banner', 'Thor Odinson', 'Wanda Maximoff', 'Scott Lang', 'Stephen Strange']
    assert concatFirstAndLastNames(first_names2,last_names2) == ['Bruce Wayne', 'Clark Kent', 'Diana Prince', 'Barry Allen', 'Hal Jordan', 'Oliver Queen', 'Arthur Curry', 'Victor Stone', 'Billy Batson', 'John Constantine']

