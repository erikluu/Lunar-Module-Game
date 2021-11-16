import math


def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n")
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.\n")
   print("   Good luck and may the force be with you!\n")
   

def getFuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   while(fuel <= 0):
      print("ERROR: Amount of fuel must be positive, please try again")
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   return fuel


def getAltitude():
   altitude = int(input("Enter the initial altitude of the LM (in meters): "))
   while(altitude <= 0 or altitude > 9999):
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      altitude = int(input("Enter the initial altitude of the LM (in meters): "))
   return altitude


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):

   #elapsedTime = elapsedTime # plus 1?? WHY DID I PUT THESE HERE??
   #fuelAmount = fuelAmount - fuelRate
   #altitude = altitude + velocity

   if(elapsedTime == 0):
      print("\nLM state at retrorocket cutoff")
   print(f"Elapsed Time: {elapsedTime:4} s")
   print(f"        Fuel: {fuelAmount:4} l")
   print(f"        Rate: {fuelRate:4} l/s")
   print(f"    Altitude: {altitude:7.2f} m")
   print(f"    Velocity: {velocity:7.2f} m/s")


def getFuelRate(currentFuel):
   fuelUsed = int(input("\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   
   while(fuelUsed > 9 or fuelUsed < 0):
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      fuelUsed = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
      
   return min(fuelUsed, currentFuel)
 

def updateAcceleration(gravity, fuelRate):
   return (gravity * ((fuelRate/5) - 1))
	

def updateAltitude(altitude, velocity, acceleration):
   newAlt = altitude + velocity + (acceleration/2)
   if(newAlt < 0):
      return 0
   else:
      return newAlt


def updateVelocity(velocity, acceleration):
   return velocity + acceleration


def updateFuel(fuel, fuelRate):
    x = fuel - fuelRate
    if(x <= 0):
    	return 0
    else:
    	return x


def displayLMLandingStatus(velocity):
   if(velocity <= 0 and velocity >= -1):
      print("\nStatus at landing - The eagle has landed!")
   if(velocity < -1 and velocity > -10):
      print("\nStatus at landing - Enjoy your oxygen while it lasts!")
   if(velocity <= -10):
      print("\nStatus at landing - Ouch - that hurt!")
