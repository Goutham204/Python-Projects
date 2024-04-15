class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calc_add(self):
        add = self.x + self.y
        return add
    def calc_sub(self):
        sub = self.x - self.y
        return sub
    def calc_multi(self):
        multi = self.x * self.y
        return multi
    def calc_div(self):
        try:
            div = (self.x / self.y)
            # if self.y !=0:
            return div
        except ZeroDivisionError:
            print("Cannot divisible by 0")

x = int(input("Enter the Number1: "))
y = int(input("Enter the Number2: "))

calculator = Calculator(x,y)
result_add = calculator.calc_add()
result_sub = calculator.calc_sub()
result_multi = calculator.calc_multi()
result_div = calculator.calc_div()

print("Sum of number: ",result_add)
print("Difference of number: ",result_sub)
print("Multiplication of number: ",result_multi)
print("Divide of the number: ",result_div) 
