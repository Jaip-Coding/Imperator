import re
import random

class Interpreter:
    def __init__(self, tokens, variables):
        self.index = 0
        self.tokens = tokens
        self.variables = variables
        self.is_interpret = False
        self.lines = {}
        self.marks = {}
    
    def get_lines(self):
        line_index = 1
        is_new_line = True
        for i in range(0, len(self.tokens)):
            current_line_token = self.tokens[i]
            if is_new_line:
                self.lines[line_index] = i
                if current_line_token == "\n":
                    is_new_line = True
                    line_index += 1
                else:
                    is_new_line = False
                continue
            if current_line_token == "\n":
                is_new_line = True
                line_index += 1
    
    def get_marks(self):
        is_mark = False
        is_equal = False
        for i in range(0, len(self.tokens)):
            current_line_token = self.tokens[i]
            if is_mark:
                self.marks[current_line_token] = i + 1
                is_mark = False
                continue
            if current_line_token == "@" and not is_equal:
                is_mark = True
                is_equal = False
            elif current_line_token == "=":
                is_equal = True
            else:
                is_equal = False
    
    def math(self):
        if self.current_token() in self.variables:
            number1 = float(self.variables[self.current_token()])
        else:
            number1 = float(self.tokens[self.index])
        self.consume_token()
        operator = ""
        result = 0
        if self.tokens[self.index] == "+":
            self.consume_token()
            if self.current_token() in self.variables:
                number2 = float(self.variables[self.current_token()])
            else:
                number2 = float(self.tokens[self.index])
            result = number1 + number2
        elif self.tokens[self.index] == "-":
            self.consume_token()
            if self.current_token() in self.variables:
                number2 = float(self.variables[self.current_token()])
            else:
                number2 = float(self.tokens[self.index])
            result = number1 - number2
        elif self.tokens[self.index] == "*":
            self.consume_token()
            if self.current_token() in self.variables:
                number2 = float(self.variables[self.current_token()])
            else:
                number2 = float(self.tokens[self.index])
            result = number1 * number2
        elif self.tokens[self.index] == "/":
            self.consume_token()
            if self.current_token() in self.variables:
                number2 = float(self.variables[self.current_token()])
            else:
                number2 = float(self.tokens[self.index])
            result = number1 / number2
        else:
            print("ERROR: INVALID OPERATOR")
            return None
        
        self.consume_token()
        
        if self.index < len(self.tokens) and self.tokens[self.index] == "P":
            self.consume_token()
            print(result)
        
        return result
    
    def string(self):
        strings = []
        while True:
            if self.index < len(self.tokens):
                if self.current_token() in self.variables:
                    strings.append(str(self.variables[self.current_token()]))
                else:
                    strings.append(self.current_token())
            self.consume_token()
            if self.index < len(self.tokens) and self.current_token() == "+":
                self.consume_token()
            else:
                break
        result = ""
        for item in strings:
            new_item = item.strip("<>")
            result += str(new_item)

        if self.index < len(self.tokens) and self.current_token() == "P":
            self.consume_token()
            print(result)
        
        return result
    
    def interpret(self):
        if self.current_token() == "M":
            self.consume_token()
            self.math()
        elif self.tokens[self.index] == "V":
            self.consume_token()
            if self.tokens[self.index] not in self.variables:
                var_name = self.tokens[self.index]
                self.consume_token()
                if self.tokens[self.index] == "=":
                    self.consume_token()
                    if self.tokens[self.index] == "M":
                        self.consume_token()
                        var_value = self.math()
                        self.variables[var_name] = var_value
                    elif self.current_token()[0] == "<":
                        self.variables[var_name] = self.string()
                    elif self.current_token()[0] == "I":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == ":":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == "INT":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    self.variables[var_name] = int(input())
                                    print(self.variables[var_name])
                                else:
                                    self.variables[var_name] = int(input())
                            elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    self.variables[var_name] = float(input())
                                    print(self.variables[var_name])
                                else:
                                    self.variables[var_name] = float(input())
                            else:
                                print("ERROR: INVALID INPUT CALL")
                        else:
                            self.variables[var_name] = input()
                            if self.index < len(self.tokens) and self.current_token() == "P":
                                self.consume_token()
                                print(self.variables[var_name])
                    elif self.current_token()[0] == "$":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == "ROUND":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == ":":
                                self.consume_token()
                                self.variables[var_name] = round(float(self.current_token()))
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    print(self.variables[var_name])
                            else:
                                print("ERROR: INVALID ROUND CALL")
                        elif self.index < len(self.tokens) and self.current_token() == "RANDOM":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == ":":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "INT":
                                    self.consume_token()
                                    if self.index < len(self.tokens) and self.current_token() == ";":
                                        self.consume_token()
                                        if self.index < len(self.tokens) and self.current_token() == "(":
                                            self.consume_token()
                                            number1 = int(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            number2 = int(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            self.variables[var_name] = random.randrange(number1, number2)
                                            if self.index < len(self.tokens) and self.current_token() == "P":
                                                self.consume_token()
                                                print(self.variables[var_name])
                                elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                                    self.consume_token()
                                    if self.index < len(self.tokens) and self.current_token() == ";":
                                        self.consume_token()
                                        if self.index < len(self.tokens) and self.current_token() == "(":
                                            self.consume_token()
                                            number1 = float(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            number2 = float(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            self.variables[var_name] = float(random.uniform(number1, number2))
                                            if self.index < len(self.tokens) and self.current_token() == "P":
                                                self.consume_token()
                                                print(self.variables[var_name])
                            else:
                                print("ERROR: INVALID RANDOM CALL")
                    else:
                        self.variables[var_name] = float(self.current_token())
                        self.consume_token()
            else:
                print("ERROR: VARIABLE ALREADY EXISTS")
        elif self.current_token()[0] == "<":
            self.string()
        elif self.tokens[self.index] == "NEW":
            self.consume_token()
            if self.tokens[self.index] in self.variables:
                var_name = self.tokens[self.index]
                self.consume_token()
                if self.tokens[self.index] == "=":
                    self.consume_token()
                    if self.tokens[self.index] == "M":
                        self.consume_token()
                        var_value = self.math()
                        self.variables[var_name] = var_value
                    elif self.current_token()[0] == "<":
                        self.variables[var_name] = self.string()
                    elif self.current_token() == "I":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == ":":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == "INT":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    self.variables[var_name] = int(input())
                                    print(self.variables[var_name])
                                else:
                                    self.variables[var_name] = int(input())
                            elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    self.variables[var_name] = float(input())
                                    print(self.variables[var_name])
                                else:
                                    self.variables[var_name] = float(input())
                            else:
                                print("ERROR: INVALID INPUT CALL")
                        else:
                            self.variables[var_name] = input()
                            if self.index < len(self.tokens) and self.current_token() == "P":
                                self.consume_token()
                                print(self.variables[var_name])
                    elif self.current_token() == "$":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == "ROUND":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == ":":
                                self.consume_token()
                                self.variables[var_name] = round(float(self.current_token()))
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    print(self.variables[var_name])
                            else:
                                print("ERROR: INVALID ROUND CALL")
                        elif self.index < len(self.tokens) and self.current_token() == "RANDOM":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == ":":
                                self.consume_token()
                                if self.index < len(self.tokens) and self.current_token() == "INT":
                                    self.consume_token()
                                    if self.index < len(self.tokens) and self.current_token() == ";":
                                        self.consume_token()
                                        if self.index < len(self.tokens) and self.current_token() == "(":
                                            self.consume_token()
                                            number1 = int(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            number2 = int(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            self.variables[var_name] = random.randrange(number1, number2)
                                            if self.index < len(self.tokens) and self.current_token() == "P":
                                                self.consume_token()
                                                print(self.variables[var_name])
                                elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                                    self.consume_token()
                                    if self.index < len(self.tokens) and self.current_token() == ";":
                                        self.consume_token()
                                        if self.index < len(self.tokens) and self.current_token() == "(":
                                            self.consume_token()
                                            number1 = float(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            number2 = float(self.current_token())
                                            self.consume_token()
                                            self.consume_token()
                                            self.variables[var_name] = float(random.uniform(number1, number2))
                                            if self.index < len(self.tokens) and self.current_token() == "P":
                                                self.consume_token()
                                                print(self.variables[var_name])
                            else:
                                print("ERROR: INVALID RANDOM CALL")
                    else:
                        self.variables[var_name] = float(self.current_token())
                        self.consume_token()
            else:
                print("ERROR: VARIABLE DOESN'T EXIST")
        elif self.current_token() == "$":
            self.consume_token()
            if self.index < len(self.tokens) and self.current_token() == "ROUND":
                self.consume_token()
                if self.index < len(self.tokens) and self.current_token() == ":":
                    self.consume_token()
                    result = round(float(self.current_token()))
                    self.consume_token()
                    if self.index < len(self.tokens) and self.current_token() == "P":
                        self.consume_token()
                        print(result)
                else:
                    print("ERROR: INVALID ROUND CALL")
            elif self.index < len(self.tokens) and self.current_token() == "RANDOM":
                self.consume_token()
                if self.index < len(self.tokens) and self.current_token() == ":":
                    self.consume_token()
                    if self.index < len(self.tokens) and self.current_token() == "INT":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == ";":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == "(":
                                self.consume_token()
                                number1 = int(self.current_token())
                                self.consume_token()
                                self.consume_token()
                                number2 = int(self.current_token())
                                self.consume_token()
                                self.consume_token()
                                result = random.randrange(number1, number2)
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    print(result)
                    elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                        self.consume_token()
                        if self.index < len(self.tokens) and self.current_token() == ";":
                            self.consume_token()
                            if self.index < len(self.tokens) and self.current_token() == "(":
                                self.consume_token()
                                number1 = float(self.current_token())
                                self.consume_token()
                                self.consume_token()
                                number2 = float(self.current_token())
                                self.consume_token()
                                self.consume_token()
                                result = float(random.uniform(number1, number2))
                                if self.index < len(self.tokens) and self.current_token() == "P":
                                    self.consume_token()
                                    print(result)
                else:
                    print("ERROR: INVALID RANDOM CALL")
        elif self.current_token() == "I":
            self.consume_token()
            if self.index < len(self.tokens) and self.current_token() == ":":
                self.consume_token()
                if self.index < len(self.tokens) and self.current_token() == "INT":
                    self.consume_token()
                    if self.index < len(self.tokens) and self.current_token() == "P":
                        self.consume_token()
                        result = int(input())
                        print(result)
                    else:
                        result = int(input())
                elif self.index < len(self.tokens) and self.current_token() == "FLOAT":
                    self.consume_token()
                    if self.index < len(self.tokens) and self.current_token() == "P":
                        self.consume_token()
                        result = float(input())
                        print(result)
                    else:
                        result = float(input())
                else:
                    print("ERROR: INVALID INPUT CALL")
            else:
                result = input()
                if self.index < len(self.tokens) and self.current_token() == "P":
                    self.consume_token()
                    print(result)
        elif self.current_token() == "IF":
            self.consume_token()
            if_val = ""
            if self.current_token() in self.variables:
                if_val = str(self.variables[self.current_token()])
                self.consume_token()
            else:
                if_val = str(self.current_token())
                self.consume_token()
            if self.current_token() == "=":
                self.consume_token()
                sec_if_val = ""
                if self.current_token() in self.variables:
                    sec_if_val = str(self.variables[self.current_token()])
                else:
                    sec_if_val = str(self.current_token())
                if if_val.isdecimal():
                    if_val_float = float(if_val)
                    if_val = str(if_val_float)
                if sec_if_val.isdecimal():
                    sec_if_val_float = float(sec_if_val)
                    sec_if_val = str(sec_if_val_float)
                self.consume_token()
                if self.current_token() == "-":
                    self.consume_token()
                    if self.current_token() == ">":
                        self.consume_token()
                        if_val = if_val.strip("<>")
                        sec_if_val = sec_if_val.strip("<>")
                        if if_val == sec_if_val:
                            self.is_interpret = True
                            self.interpret()
                            self.is_interpret = False
                        else:
                            while self.index < len(self.tokens) and self.current_token() != "\n":
                                self.consume_token()
                            self.consume_token()
            elif self.current_token()[0] == "<":
                self.consume_token()
                print("ERROR: '<' DOESN'T EXIST. USE '>'")
            elif self.current_token() == ">":
                self.consume_token()
                sec_if_val = ""
                if self.current_token() in self.variables:
                    sec_if_val = float(self.variables[self.current_token()])
                else:
                    sec_if_val = float(self.current_token())
                self.consume_token()
                if self.current_token() == "-":
                    self.consume_token()
                    if self.current_token() == ">":
                        self.consume_token()
                        if float(if_val) > sec_if_val:
                            self.interpret()
                        else:
                            while self.index < len(self.tokens) and self.current_token() != "\n":
                                self.consume_token()
                            self.consume_token()
            elif self.current_token() == "!":
                self.consume_token()
                sec_if_val = ""
                if self.current_token() in self.variables:
                    sec_if_val = str(self.variables[self.current_token()])
                else:
                    sec_if_val = str(self.current_token())
                if sec_if_val.isdecimal():
                    sec_if_val_float = float(sec_if_val)
                    sec_if_val = str(sec_if_val_float)
                self.consume_token()
                if self.current_token() == "-":
                    self.consume_token()
                    if self.current_token() == ">":
                        self.consume_token()
                        if_val = if_val.strip("<>")
                        sec_if_val = sec_if_val.strip("<>")
                        if if_val != sec_if_val:
                            self.is_interpret = True
                            self.interpret()
                            self.is_interpret = False
                        else:
                            while self.index < len(self.tokens) and self.current_token() != "\n":
                                self.consume_token()
                            self.consume_token()
            else:
                print("ERROR: INVALID IF CALL")
        elif self.current_token() == "!":
            self.consume_token()
            if self.current_token() == "!":
                self.consume_token()
                if self.current_token() == "!":
                    self.consume_token()
                    while self.index < len(self.tokens) and self.current_token() != "\n":
                        self.consume_token()
        elif self.current_token() == "REPEAT":
            self.consume_token()
            repeat_val = int(self.current_token())
            self.consume_token()
            if self.current_token() == "[":
                self.consume_token()
                start_pos = self.index
                self.is_interpret = True
                for i in range(0, repeat_val):
                    self.index = start_pos
                    while self.index < len(self.tokens) and self.current_token() != "]":
                        self.interpret()
                    self.consume_token()
                self.is_interpret = False
        elif self.current_token() == "SOURCE":
            self.consume_token()
            source_file = ""
            while self.index < len(self.tokens) and self.current_token() != "\n":
                source_file += self.current_token()
                self.consume_token()
            self.consume_token()
            source_file_new = source_file + ".impr"
            file_content = ''
            with open(source_file_new, 'r') as file:
                file_content = file.read()
                file.close()
            file_tokens = re.findall(r'<.*?>|\d+\.\d+|\d+|[A-Za-z]+|\S|\n', file_content)
            file_variables = {}
            interpreter = Interpreter(file_tokens, file_variables)
            interpreter.get_lines()
            interpreter.get_marks()
            interpreter.interpret()
        elif self.current_token() == "\n":
            self.consume_token()
        elif self.current_token() == "%":
            self.consume_token()
            if self.current_token() == "=":
                self.consume_token()
                if self.current_token() == "(":
                    self.consume_token()
                    new_line_1 = int(self.current_token())
                    self.consume_token()
                    if self.current_token() == ",":
                        self.consume_token()
                        new_line_2 = int(self.current_token())
                        self.consume_token()
                        if self.current_token() == ")":
                            self.consume_token()
                            start_index = self.index
                            self.index = self.lines[new_line_1]
                            new_line_2_index = self.lines[new_line_2 + 1]
                            while self.index < len(self.tokens) and self.index != new_line_2_index:
                                self.is_interpret = True
                                self.interpret()
                                self.is_interpret = False
                            self.index = start_index
                elif self.current_token() == "@":
                    self.consume_token()
                    new_line = self.marks[str(self.current_token())]
                    self.consume_token()
                    self.index = new_line
                else:
                    new_line = int(self.current_token())
                    self.consume_token()
                    self.index = self.lines[new_line]
        elif self.current_token() == "#":
            self.consume_token()
            if self.current_token() == "STOP":
                self.consume_token()
                exit(1)
        elif self.current_token() in self.variables:
            var_name = self.current_token()
            self.consume_token()
            if self.index < len(self.tokens) and self.current_token() == "P":
                self.consume_token()
                print(self.variables[var_name])
        
        if self.index < len(self.tokens) and not self.is_interpret:
            self.interpret()

    def consume_token(self):
        self.index += 1
    
    def current_token(self):
        return self.tokens[self.index]

variables = {}

while True:
    user_input = input()
    tokens = re.findall(r'<.*?>|\d+\.\d+|\d+|[A-Za-z]+|\S|\n', user_input)
    interpreter = Interpreter(tokens, variables)
    interpreter.get_lines()
    interpreter.get_marks()
    interpreter.interpret()