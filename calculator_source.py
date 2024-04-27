class CalculatorOperations:
    def addition(x , y):
        return format(x + y, ".2f")

    def subtraction(x , y):
        return format(x - y, ".2f")

    def multiplication(x , y):
        return format(x * y, ".2f")

    def division(x , y):
        if (y == 0):
            print ("ERROR, divison by 0")
            return
        else:
            return format(x / y, ".2f")
        
    def percentile(x, y, operator):
        if operator == "+":    
            return format(x + x * y / 100, ".2f")
        if operator == "-":    
            return format(x - x * y / 100, ".2f")
        if operator == "/":    
            return format(x / x * y / 100, ".2f")
        if operator == "*":    
            return format(x * x * y / 100, ".2f")