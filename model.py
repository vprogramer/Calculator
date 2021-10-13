class Model:
    def __init__(self):
        self.value = ""
        self.previous_value = ""
        self.operator = ""
        self.view = ""
        self.previous_caption = ""

    def _evaluate(self):
        try:
            return eval(self.previous_value + self.operator + self.value)
        except SyntaxError:
            print('Incorrect operation')
        except ZeroDivisionError:
            print("You divided by zero")

    def calculate(self, caption):
        if caption == "C":
            self.value = ""
            self.previous_value = ""
            self.operator = ""
            self.view = ""

        elif caption == "+/-":
            self.value = self.value[1:] if self.value[0] == "-" else "-" + self.value
            self.view = self.value

        elif caption == "%":
            value = float(self.value) if "." in self.value else int(self.value)
            self.value = str(value / 100)
            self.view = self.value

        elif caption == "Del":
            self.value = self.value[:len(self.value)-1]
            self.view = self.value

        elif caption == "=":
            self.view = ""
            if self.operator == "Pow":
                self.previous_value = str(pow(float(self.previous_value), float(self.value)))
                self.view = self.previous_value
            elif self._evaluate() is not None:
                self.previous_value = str(self._evaluate())
                self.view = self.previous_value

        elif caption == ".":
            if caption not in self.value:
                self.value += str(".")
                self.view = self.value

        elif isinstance(caption, int):
            self.value += str(caption)
            self.view = self.value

        else:
            if self.value:
                self.operator = str(caption)
                if self.previous_caption != "=":
                    self.previous_value = self.value
                self.value = ""
                self.view = caption

        self.previous_caption = caption
        # print(str(self.previous_value), str(self.operator), str(self.value), "|", caption)
        return self.view

