
def wind_chill(T, V):
    chill_number = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return chill_number
def celsius_conversion(C):
    T = (9/5) * C + 32 
    return T 
def fahrenheit_conversion(convert):
    conversion = (5/9) * convert - 32
    return conversion
choice = 'y'
while choice != 'n':
    V = 5
    Temp = float(input("What is the temperature? "))
    unit_selection = input("Is this temperature in Fahrenheit or Celcius (F/C)? ").upper()
    if unit_selection == 'F':
        unit = 'Fahrenheit'
        T = Temp
        print('')
        print(f"The wind chill at {Temp} degrees {unit} with a wind speed of: ")
        print('')
        while V < 60:
            print(f"    {V} mph is {wind_chill(T, V):.2f} degrees {unit}.")
            V += 5
    elif unit_selection == 'C':
        unit = 'Celcius'
        C = Temp
        T = celsius_conversion(C)
        print (T)
        print('')
        print(f"The wind chill at {Temp} degrees {unit} with a wind speed of: ")
        print('')
        while V < 60:
            convert = wind_chill(T, V)
            conversion = fahrenheit_conversion(convert)

            print(f"    {V} mph is {conversion:.2f} degrees {unit}.")
            V += 5
    else:
        print("Enter 'C' or 'F' and try again.")
    print('')
    choice = input("Would you like to continue? Enter 'y' or 'n'. ")
print ('Good Luck!')        

