def farenheit2celsius(c):
    return (c * 9/5) + 32
def kelvin2celsius(c):
    return c * 273.15
def rankine2celsius(c):
    return (c + 273.15) * 9/5
def main():
    c = float(input("celsius:"))
    celsius = 10
    for c in range (-30 ,60 ,10):
        celsius += 10
        print ("F:",farenheit2celsius(c),"K:",kelvin2celsius(c),"R:",rankine2celsius(c))
    if(c > -30) and (c <= -20):
        print ("Artic")
    elif(c > -19) and (c <= -10):
        print ("Baltic")
    elif(c > -9) and (c <= 2):
        print ("Freezing")
    elif (c > 3) and (c <= 10):
        print ("chilly")
    elif (c > 11) and (c <= 20):
        print ("Not Bad")
    else:
        print ("Great Summer in Ireland")

main ()


