
    
eTemp = float(input("Enter the temperature in Fahrenheit: "))
EoilLevel = float(input("Enter the oil level in liters: "))
fuelLevel = float(input("Enter the fuel level in liters: "))

if eTemp < 90 and EoilLevel > 60 and fuelLevel > 750000:
            print("Aircraft is ready for takeoff")
else:
    print("Aircraft is not ready for takeoff")
