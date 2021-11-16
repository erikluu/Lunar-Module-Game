from landerFuncs import *


def main():

	showWelcome()
	# Initial Variables: Time, Altitude, Velocity, Fuel, Fuel Rate, Acceleration
	time = 0
	altitude = float(getAltitude())
	velocity = float(0)
	fuel = getFuel()
	fuelRate = 0
	acceleration = float(0)

	# First Display of LM State
	displayLMState(time, altitude, velocity, fuel, fuelRate)

	while(altitude != 0):
		if(fuel > 0):
			fuelRate = getFuelRate(fuel)
			acceleration = updateAcceleration(1.62, fuelRate)
			altitude = updateAltitude(altitude, velocity, acceleration)
			velocity = updateVelocity(velocity, acceleration)
			fuel = updateFuel(fuel, fuelRate)
			time+=1
			
			if(fuel > 0 and altitude != 0):
				displayLMState(time, altitude, velocity, fuel, fuelRate) # Prints to Screen

		else:
			print("OUT OF FUEL", end=' - ')
			print(f"Elapsed Time: {time:3} ", end='')
			print(f"Altitude: {altitude:7.2f} ", end='')
			print(f"Velocity: {velocity:7.2f} ")
			fuelRate = 0
			acceleration = updateAcceleration(1.62, fuelRate)
			altitude = updateAltitude(altitude, velocity, acceleration)
			velocity = updateVelocity(velocity, acceleration)
			time+=1
			
	print("\nLM state at landing/impact")
	displayLMState(time, altitude, velocity, fuel, fuelRate)
	displayLMLandingStatus(velocity)


if __name__ == '__main__':
   main()