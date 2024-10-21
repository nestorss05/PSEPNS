#coding: latin1
class Calculo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        res = self.num1 + self.num2
        return res

    def resta(self):
        res = self.num1 - self.num2
        return res

    def multp(self):
        res = self.num1 * self.num2
        return res

    def divi(self):
        if self.num2 != 0:
            res = self.num1 / self.num2
        return res