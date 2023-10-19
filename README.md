# Imperator
An 80s-like programming language.

## About
"Imperator" is an 80s-like programming language created in 2023.

## Syntax
A brief overview of the syntax of "Imperator":

"Imperator" is an imperative language - where the name comes from.

### Print
Values can be printed by typing ```P``` at the end of the line.

### Calculations
Calculations can be called with ```M```. "Imperator" supports only 2-number-calculations. The value of the calculation can be printed with ```P```

Example: ```M 1+2 P``` 

The number "3" will be output

Imperator also supports calculations with variables: ```M a+b P```

### Strings
Strings are written with a ```<``` at the beginning and a ```>``` at the end.

Example: ```<Hello, World!> P```

Variables can also be added to strings.

Example: ```<Number: > + a P```

### Variables
Imperator supports string and number variables.

**Declare variables**

The letter to declare a variable is ```V```

Declare a variable: ```V``` + name + ```=``` + statement

Example: ```V test = 1```

Example 2: ```V math = M 1+1```

Example 3: ```V string = <Test>```

**Change variables**

Changing variables works in the same as declaring variables, but the keyword is ```NEW```

Example: ```NEW test = 2```

### Loops
The keyword for loops in Imperator is ```REPEAT```

**Example:** 
```
REPEAT 5 [
M 1+1 P
]
```
This will output "2" for five times.

**Example 2:**
```
V i = 0
REPEAT 5 [
NEW i = i + 1
i P
]
```
This will output:
```
1
2
3
4
5
```

### If statement
You can call an if statement in Imperator as follows:
```IF``` + expression + ```->``` + statement

**Operator: =**

With ```=``` you can check if two values are the same.

Example: ```IF a = 10 -> <Same value!> P```

**Operator: >**

With ```>``` you can check if a values is greater than a other one. ```<``` doesn't exist

Example: ```IF a > 10 -> <a is greater than 10!> P```

**Operator: !**

With ```!``` you can check if two values are not the same.

Example: ```IF a ! 10 -> <a is not 10!> P```

### Input
You can ask the user for a input with the keyword ```I```

**String inputs**

Example: ```V string = I```

**Int inputs**

Example: ```V int = I : INT```

**Float inputs**

Example: ```V float = I : FLOAT```

### Round function
Numbers can be rounded with ```$ROUND```

Example: ```V roundedNumber = $ROUND : 1.5```

### Random function
Random numbers can be generated with ```$RANDOM```

**Random ints**

Example: ```V randInt = $RANDOM : INT ; (1, 5)```

This will generate a random int between 1 and 5

**Random floats**

Example: ```V randFloat = $RANDOM : FLOAT ; (1, 5)```

This will generate a random float between 1 and 5

### Jump to lines
Imperator can jump to a new line with ```%```

**Line numbers**

To jump to a line by their line number, you have to write: ```% =``` + line number

Example: ```% = 5```

The program will jump to line 5

**Ranges**

With ranges Imperator can jump to a line and interpret everything until the other line. Then Imperator will jump back to the line where the range was called.

Example: ```% = (5, 7)```

This will interpret the line 5 to 7 and will then jump back and continue

**Marks**

Imperator also contains a feature called marks. You can add a mark by typing ```@``` + name. Then you can call a mark like this: ```% = @``` + name. Imperator will jump to the line where you added the mark. This can be helpful if the line numbers are changing often because of edits in your code.

Example:
```
% = @Test

<This will not be output> P

@Test
<This will be output> P
```

### Stop the script
To stop the script you simply have to write ```#STOP```. The script will stop immediately if it encounters this keyword

## Access and run Imperator files
You can access and run Imperator files with ```SOURCE``` + file name (without file extension). Make sure that the file has the file extension ```.impr```

**Example:** ```SOURCE TEST```

This will access and run the file ```TEST.impr```
