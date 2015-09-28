def average_numbers( a , b , c):
    average_numbers = (a + b + c) / 3
    return average_numbers


def main ( ):
    a = int (input ("enter a:"))
    b = int (input ("enter b:"))
    c = int (input ("enter c:"))
    average = average_numbers(a , b , c )
    print ("average numbers :" , average)

main()
