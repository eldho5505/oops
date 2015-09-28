def perimeter_of_rectangle(length,width):
    perimeter_of_rectangle = 2 * (length + width)
    return perimeter_of_rectangle

def area_of_rectangle(length,width):
    area_of_rectangle = length * width
    return area_of_rectangle

def main():
    length = int(input("enter the length:"))
    width = int(input("enter the width:"))
    perimeter = perimeter_of_rectangle(length,width)
    area = area_of_rectangle(length,width)
    print ("perimeter_of_rectangle:", int(perimeter))
    print ("area_of_rectangle :", int(area))

main ()
