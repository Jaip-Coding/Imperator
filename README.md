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
This will output "2" for four times.

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
