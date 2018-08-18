# H6_sung.py
# Kinetic Energy: excercising function decomposition and later aggregation in more sophiticated way
# in example of Kinetic Energy computation

def do_convert(distance, mass):
    """
        convert from user inputs in main function to SI system for return with new variables
    """
    distance_meter = distance * 0.3048
    mass_kg = mass * 0.453592

    return distance_meter, mass_kg

def calc_time(distance_meter):
    """
        calculate time from the given formula
        due to gravitational constant, time should be in sec(s) for return
    """
    time = (2 * distance_meter/9.8)**(1/2)

    return time

def calc_velocity(time):
    """
        calculate the speed(velocity) in m/s from the results from the the functions above that feed time and new distance in meter
    """
    velocity = 9.8 * time
    return velocity

def kinetic_energy(velocity, mass_kg):
    """
        calculate the kinetic energy for return;
        return unit should be in Joules,
        if mass is in kg, speed is in (m/s)^2
    """
    energy = 0.5 * mass_kg * velocity ** 2
    return energy

def display_results(energy):
    """
        pure reporting function, as instucted, the results only displayed
    """
    print('The calculated Kinetic Energy is: ', '{:,.2f}'.format(energy), 'Joules')

def main():
    """
        set prompting function in main()
        Return: after prompting, numeric values from the functions will be registered in float
    """
    
    distance = float(input('Please Enter the distance from the ground in feet: '))
    mass = float(input('Please Enter the mass in pounds: '))

    distance_meter, mass_kg = do_convert(distance, mass)
    time = calc_time(distance_meter)
    velocity = calc_velocity(time)
    energy = kinetic_energy(velocity, mass_kg)
    display_results(energy)

if __name__ == '__main__':
    main()

# 7/19

