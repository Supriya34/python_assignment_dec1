def area(radius = 0):
    return (22/7)*radius*radius

radius = float(input("Enter the radius of a circle "))

print("The area of circle whose radius is {0} = {1:.3f} ".format(radius,area(radius)))