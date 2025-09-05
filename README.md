# Python Coding Challenges

Fork and clone this repo.
### Optional if you want to run the pytests to check your work.
In your terminal run
```
pip3 install pytest
```
To run the tests run
```
pytest test_<name_of_file>.py
```
replace `<name_of_file>` with the name of the file you want to test.

## Challenge 1: `binaryToDecimal(binaryStr)`
[How to Convert Binary Into Decimal (and Vice Versa)](https://science.howstuffworks.com/math-concepts/binary-to-decimal.htm)

Write a function called `binaryToDecimal` that takes a parameter called `binaryStr`. When the function is called it takes a binary number represented as a string. Then function returns a decimal integer that is equivalent to the binary number.

### example calls
```python
print(binaryToDecimal("1010"))
print(binaryToDecimal("11"))
print(binaryToDecimal("100"))
print(binaryToDecimal("0"))
print(binaryToDecimal("1111"))
```
**OUTPUT:** 
```
10
3
4
0
15
```

## Challenge 2: `decimalToBinary(integer)`

Write a function called `decimalToBinary` that takes a parameter called `integer`. When the function is called it takes an integer as an arguement and returns a sting of the equivalent binary number. You will have to handle all positive integers and zero. **hint:** zero will have to be handled separately from other numbers.
### example calls
```python
print(decimalToBinary(15))
print(decimalToBinary(9))
print(decimalToBinary(21))
print(decimalToBinary(5))
```

**OUTPUT**
```
1111
1001
10101
101
```

## Challenge 3: `concatFirstAndLastNames(firstNames,lastNames)`

Write a function called `concatFirstAndLastNames` that takes two parameters `firstNames` and `lastNames`. When the function is called it takes a list of first names and a list of last names as arguments. The function iterates over each name in both lists and concatenates the matching index from both lists into a full name and add the full name to a new list. Then it returns the new list of full names. You can assume that the lists will always be the same length, and that the names are properly capitalized.

### example calls:
```python
first_names = ['Carol','Reed','Steve','Natasha','Clint','Wanda','Tony']
last_names = ['Danvers','Richards','Rogers','Romanoff','Barton','Maximoff','Stark']
print(concatFirstAndLastNames(first_names,last_names))
```
**OUTPUT**
```
['Carol Danvers', 'Reed Richards', 'Steve Rogers', 'Natasha Romanoff', 'Clint Barton', 'Wanda Maximoff', 'Tony Stark']
```

## Challenge 4: `avgGrade(grades)`

 Write a function called `avgGrade` that takes one paramenter `grades`. When the function is called it takes a list of numbers. It calculates the average grade based on the numbers in the list. The function returns the average as a float rounded to the 1st decimal place.

### example calls:
```python
grades1 = [52, 59, 81, 74, 72, 88, 76, 71, 99, 95]
grades2 = [61, 92, 63, 62, 76, 89, 59, 96, 61, 78]
grades3 = [98, 62, 54, 96, 85, 89, 68, 51, 79, 89]

print(avgGrade(grades1))
print(avgGrade(grades2))
print(avgGrade(grades3))
```

**OUTPUT**
```
76.7
73.7
77.1
```
