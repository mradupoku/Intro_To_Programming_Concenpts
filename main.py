PI = 3.1416

#Functions
def circle_area(radius):
    return PI * radius ** 2


def total_due(money, tax_rate):
    return money + (money * tax_rate)


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


#Main Program

# Area of Circle
radius = float(input("Enter radius: "))
area = circle_area(radius)
print("Area:", format(area, ".2f"))

# Temperature Conversion
fahrenheit = float(input("Enter Fahrenheit temperature: "))
celsius = to_celsius(fahrenheit)
print("Celsius:", format(celsius, ".5f"))