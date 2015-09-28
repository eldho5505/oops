def convert_celsiustofarnheit(tempincelcius):
    #formula = c * 9/5 + 32
    tempinfarenheit = tempincelcius * 9/5 + 32
    return tempinfarenheit

def main():
    tempincelcius = float(input ("Enter temperature in degree celcius:"))
    tempinfarenheit = convert_celsiustofarnheit(tempincelcius)
    print("tempinfarenheit: ", float(tempinfarenheit))

main()
