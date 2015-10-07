def farenheit2celsius(c):
    return round(c * 9/5) + 32
def kelvin2celsius(c):
    return round(c * 273.15)
def rankine2celsius(c):
    return round(c + 273.15) * 9/5
def main():
    c = float(input("celsius:"))
    celsius = 10
    for c in range (-30 ,60 ,10):
        celsius += 10
        print ("F:",farenheit2celsius(c),"K:",kelvin2celsius(c),"R:",rankine2celsius(c))
main ()


